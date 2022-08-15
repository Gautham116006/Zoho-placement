'''
5 if perfect square.
4 if  multiple of 4 and divisible by 6
3 if even
print arr based on weight in ascending order.
'''
import math
import math

arr = [10, 36, 54, 89, 12]

def weight_sort(arr):
    a = []
    for i in arr:
        weight = 0
        if math.ceil(math.sqrt(i)) == math.floor(math.sqrt(i)):
            print()
            weight += 5
        if i % 4 == 0 and i % 6 == 0:
            weight += 4
        if i % 2 == 0:
            weight += 3
        a.append((i, weight))
        a.sort(key=lambda x : x[1])

    for i in a:
        print(f'<{i[0]}, {i[1]}>', end=" ")


weight_sort(arr)



