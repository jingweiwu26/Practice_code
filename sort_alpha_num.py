def sort_alphanumeric(arr):
    size=len(arr)
    arr=list(arr)
    for i in range(size - 1):
        for j in range(size - 1):
            if arr[j] > arr[j + 1] and arr[j].isalpha() == arr[j + 1].isalpha():
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return ''.join(arr)

