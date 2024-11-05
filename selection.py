# Sorting technique for Selection Sort

def selection_sort(list):
    n = len(list)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if list[j]<list[min_index]:
                min_index = j
        list[i],list[min_index] = list[min_index],list[i]


lis = [32,12,43,23,42,54,53,23,54]
selection_sort(lis)
print(lis)            
    