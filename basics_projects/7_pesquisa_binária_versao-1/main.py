from random import randint

def binary_search(list, element, low=None, high=None):
    if low is None:
        low = 0 
    if high is None:
        high = len(list) - 1
    
    elif high < low:
        return -1
    
    midElement = (low + high) // 2
    
    if list[midElement] > element:
        return binary_search(list, element, low, (midElement-1))
    
    elif list[midElement] < element:
        return binary_search(list, element, (midElement+1), high)
    
    else:
        return midElement
    
if __name__ == '__main__':
    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(randint(-1*length, 2*length))
    sorted_list = sorted(list(sorted_list))

    a = binary_search(sorted_list, 1000)
    print(a)
