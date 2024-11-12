# Program for Quick Sort

def quick_sort(list):
    if len(list)<=1:
        return list
    else:
        pivot = list[0]    
        lesser = [x for x in list [1:] if x<=pivot]
        greater = [x for x in list [1:] if x>pivot]
        return quick_sort(lesser)+[pivot]+quick_sort(greater)
    
my_list = [34,34,232,14,54,654,325,32]
my_list = quick_sort(my_list)
print(my_list)    