class LRUCache(object):
    
    class Node(object):
        def __init__(self, key, val):
            self.previous = None
            self.next = None
            self.key = key
            self.val = val

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dict={}
        self.capacity= capacity
        self.size = 0
        self.head = self.Node(-1,-1)
        self.tail = self.Node(-1,-1)
        self.head.next = self.tail
        self.tail.previous = self.head

        
    def insert(self, node):
        node.previous = self.head
        node.next=self.head.next
        self.head.next.previous=node
        self.head.next=node

    def remove(self, node):
        node.previous.next=node.next
        node.next.previous=node.previous
        node.previous, node.next = None, None
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dict:
            return -1
        node = self.dict[key]
        self.remove(node)
        self.insert(node)
        return node.val


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dict:
            node = self.dict[key]
            self.remove(node)
            self.insert(node)
            node.val = value
          
        else:
            if self.size == self.capacity:
                discard = self.tail.previous
                self.remove(discard)
                del self.dict[discard.key]
                self.size -= 1 

            node = self.Node(key, value)
            self.dict[key] = node
            self.insert(node)
            self.size += 1
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dic = collections.OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        
        if key not in self.dic:
            return -1
        self.dic[key] = self.dic.pop(key, None)
        return self.dic.get(key)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dic:
            self.dic.pop(key, None)
            self.dic[key] = value
            
        elif len(self.dic) >= self.capacity:
            self.dic.popitem(0)
            self.dic[key] = value
            
        elif len(self.dic) < self.capacity:
            self.dic[key] = value
