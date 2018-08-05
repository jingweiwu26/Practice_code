# -*- coding: utf-8 -*-
"""
Created on Fri Aug 03 16:57:04 2018

@author: Andrew Wu
"""
import datetime
import logging
from itertools import count
from collections import namedtuple

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns



class Calculation(object):
    
    def __init__(self, request_date, freq_mapping):
        self.request_date = request_date
        self.freq_mapping = freq_mapping

    def evaluate(self):
        """
        Main logic of the calculation
        """
        df = (self.get_merged_df()
                  .pipe(self.get_tranche_data))
        return df

    def get_merged_df(self):
        """
        Read the two sheets from the input file and merge.
        Returns: df
        """
        input_file = pd.ExcelFile('MIO_Liquidity_Model_Case.xlsx')
        terms_df = (input_file.parse('Fund Terms')
                              .rename(columns={'Fund Name': 'fund_name',
                                               'Redemption Frequency': 'frequency',
                                               'Settlement Period': 'settlement_period',
                                               'Gate': 'gate',
                                               'Lockup': 'lockup'}))

        # Convert the frequency to numeric
        terms_df['frequency'] = terms_df['frequency'].map(self.freq_mapping)
        # This mapping is actually dangerous, imagine somehow there is a `Bimonthly` in the file that we didnt know when run this calc
        if terms_df['frequency'].isnull().any():
            logging.ERROR('Unmapped the frequency, please check file content')
            self.exitcode = 1
            return pd.DataFrame()

        invest_df = (input_file.parse('Tranche Investment Data')
                               .rename(columns={'Fund Name': 'fund_name',
                                                'Date of Investment': 'investment_date',
                                                'Net Asset Value' : 'nav'}))
        
        # There is a NaN value on terms sheet for Fund 5 on Gate, 
        # Assume it means there is no restriction on that but better check
        df = (invest_df.merge(terms_df, how='left', on='fund_name')
                       .fillna({'gate': 1.0}))
        
        return df

    def get_tranche_data(self, df):
        """
        Prcess df, get tranche level cash flow amount, receive date and remain balance
        """
        # Create a tranche name for each fund
        # Format tranche name as Fund_n_tranche_n
        df['tranche_name'] = (df['fund_name'].str.replace(" ", "_") 
                              + '_tranche_' 
                              + (df.groupby(['fund_name']).cumcount()+1).astype(str))        
        
        # Create lockup_release_date
        df['lockup_release_date'] = df.apply(lambda row: row['investment_date'] + pd.Timedelta(row['lockup'], unit='M'), axis=1).dt.floor('d')

        # Create gate_amount, which is the maxium amount can be withdrawn at a single time
        df['gate_amount'] = df['gate'] * df['nav']

        # Separate locked tranche and released tranche
        released_tranche_df = df[df['lockup_release_date'] < self.request_date].assign(note='Open')
        locked_tranche_df = df[df['lockup_release_date'] >= self.request_date].assign(note='Locked')
        
        # Generate first cash flow date for released_tranche_df        
        released_tranche_df['first_cash_flow_date_unsettled'] = (released_tranche_df.apply(lambda row: 
                                                                                first_cash_flow_day_finder(self.request_date, row['frequency']),
                                                                                axis=1)
                                                                .dt.floor('d'))
        
        # For locked_tranches, we cannot initiate the redemption        
        # For released_tranches, generate cash_flow_df and merge back to the original
        cash_flow_df = generate_cash_flow_df(released_tranche_df)
        released_tranche_df = released_tranche_df.merge(cash_flow_df, how='left', on='tranche_name')
        
        # Concat dfs to final df
        processed_df = pd.concat([released_tranche_df, locked_tranche_df], ignore_index=True, sort=False).assign(request_date=self.request_date)
        
        # Adding a column for accumulative amount received
        processed_df['received_total'] = processed_df['nav'] - processed_df['remain_balance'] 
        
        # Store a snapshot of this df, in future this can be used to cache calculation result or save the result in db
        self._df = processed_df        
        return processed_df

    @property
    def derive_fund_level_time_to_liquidity(self):        
        df = self._df

        # Filter out locked tranches
        df = df[df['note'] != 'Locked'][['fund_name', 'receive_date', 'receive_amount']]
        
        # Convert dates_delta to float, makes it easier to take average
        df['dates_delta'] = (df['receive_date'] - self.request_date).astype('timedelta64[D]')

        # Calculate weighted average at fund level
        df['fund_sum'] = df.groupby('fund_name')['receive_amount'].transform('sum')
        df['weight'] = df['receive_amount'] / df['fund_sum']
        df['weighted_average_time_to_liquidity'] = df['dates_delta'] * df['weight']
        df = df.groupby('fund_name', as_index=False)['fund_name', 'weighted_average_time_to_liquidity'].sum()

        return df

    @property
    def derive_portfolio_level_time_to_liquidity(self):
        df = self._df
        df = df[df['note'] != 'Locked'][['fund_name', 'receive_date', 'receive_amount']]
        df['dates_delta'] = (df['receive_date'] - self.request_date).astype('timedelta64[D]')
        
         # Calculate weighted average at portfolio level
        df['portfolio_sum'] = df['receive_amount'].sum()
        df['portfolio_weight'] = df['receive_amount'] / df['portfolio_sum']
        portfolio_weighted_average_time_to_liquidity = sum(df['dates_delta'] * df['portfolio_weight'])
    
        return pd.DataFrame([portfolio_weighted_average_time_to_liquidity], columns=['portfolio_weighted_average_time_to_liquidity'])

def generate_cash_flow_df(df):
    # Given the released tranches df, returns a cash_flow_df showing records for each withdraw
    # This df will be used to merge back to the original df

    cash_flow_data = []
    record = namedtuple('record', ['tranche_name', 'receive_date', 'receive_amount', 'remain_balance', 'last_receive_date'])
    
    # Each row in the df is an unique tranche
    for index, row in df.iterrows():
        # Given an unique tranche, we use a genertor to generate all the dates that will receive a cash flow
        date_generator = generate_next_receive_date(row['first_cash_flow_date_unsettled'],
                                                    row['frequency'],
                                                    row['settlement_period'])
                                                    
        remain_balance = row['nav']
        gate_amount = row['gate_amount']
        tranche_name = row['tranche_name']
        last_receive_date = None
        receive_date = None
    
        # Multiplied with a percentage, so we end up with a float, need to handle the precision
        while not np.isclose(remain_balance, 0):
            if receive_date:
                last_receive_date = receive_date
            receive_date = date_generator.next()
            receive_amount = min(remain_balance, gate_amount)
            remain_balance -= receive_amount
            cash_flow_data.append(record(tranche_name, receive_date, receive_amount, remain_balance, last_receive_date))
    
    cash_flow_df = pd.DataFrame(cash_flow_data, columns=record._fields)
    return cash_flow_df


def generate_next_receive_date(first_cash_flow_date_unsettled, freq, settlement_period):
    # Given a first_cash_flow_date_unsettled, freq, and settlement_period, 
    # Generate next date that receives cash flow
    counter = count(start=0, step=freq)
    while True:
        next_date = (first_cash_flow_date_unsettled 
                     + pd.tseries.offsets.MonthEnd(counter.next()) 
                     + pd.Timedelta(settlement_period, unit='D'))
        yield next_date


def first_cash_flow_day_finder(request_date, freq):
    # Given a request date and freq, find the first unsettled cash flow date  
    if freq == 1:
        return request_date + pd.tseries.offsets.MonthEnd(0)
    
    request_month = request_date.month
    remainder_month = request_month % freq
    return (request_date 
            - pd.Timedelta(remainder_month, unit='M') 
            + pd.Timedelta(freq, unit='M')
            + pd.tseries.offsets.MonthEnd(0))
    
    
if __name__ == '__main__':
    # We should add the mapping here instead of hard code it in the calculation itself, 
    # In case we have other kinds of mapping, it just a configuration change
    configuration = {'request_date' : datetime.datetime(2017,5,31),
                     'freq_mapping' : {'Monthly': 1,
                                       'Quarterly': 3,
                                       'Semiannual': 6,
                                       'Annual': 12}}                                       
    calc = Calculation(**configuration)

    # Task 1A    
    cash_flow_result = calc.evaluate()
    print cash_flow_result

    # Task 1B - Lazy evaluation, in case we only need result for 1A, we do not have to calulate everything for 1B
    fund_level_time_to_liquidity = calc.derive_fund_level_time_to_liquidity
    portfolio_level_time_to_liquidity = calc.derive_portfolio_level_time_to_liquidity
    
    # Task 2A
    # Tranche level graph
    # df = cash_flow_result[cash_flow_result['note'] != 'Locked']
    # df = df[['tranche_name', 'receive_date', 'received_total']]    

    # sns.set()
    # grid = sns.FacetGrid(df, col="tranche_name", col_wrap=4, size=8)
    # grid.map(plt.plot, "receive_date", "received_total", marker="o")
    # plt.gca().yaxis.set_major_formatter(mtick.StrMethodFormatter('${x:,.0f}'))
    # plt.show() In case you want to see the graph at tranche level
    
    # Fund Level graph
    f_df = cash_flow_result[cash_flow_result['note'] != 'Locked']
    f_df = f_df[['fund_name', 'receive_date', 'received_total']]
    f_df = f_df.groupby(['fund_name', 'receive_date'], as_index=False).sum()
    grid = sns.FacetGrid(f_df, col="fund_name", col_wrap=4, size=8)
    grid.map(plt.plot, "receive_date", "received_total", marker="o")
    plt.gca().yaxis.set_major_formatter(mtick.StrMethodFormatter('${x:,.0f}'))
    plt.show()

    # Portfolio level graph
    p_df = cash_flow_result[cash_flow_result['note'] != 'Locked']
    p_df = p_df[['receive_date', 'receive_amount']].groupby('receive_date', as_index=False).sum()
    p_df = p_df.set_index('receive_date')
    p_df = p_df.resample('1M').ffill()

    sns.set(rc={'figure.figsize':(11.7,8.27)})
    ax = sns.lineplot(data=p_df, size=8)
    plt.gca().yaxis.set_major_formatter(mtick.StrMethodFormatter('${x:,.0f}'))
    plt.show()
    
    # Task 2B
    print "fund_level_weighted_average_time_to_liquidity:"
    print fund_level_time_to_liquidity

    print "portfolio_level_time_to_liquidity"
    print portfolio_level_time_to_liquidity


