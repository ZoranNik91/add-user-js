import math
def create_array(size = 11, max = 50):
    from random import randint
    return [randint(0,max) for _ in range(size)]

def merge(a, b):
    c = []
    a_idx, b_idx = 0, 0
    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] < b[b_idx]:
            c.append(a[a_idx])
            a_idx += 1
        else:
            c.append(b[b_idx])
            b_idx += 1
    if a_idx == len(a): c.extend(b[b_idx:])
    else:               c.extend(a[a_idx:])
    return c

def merge_sort(a):
    if len(a) <= 1: return a
    x = math.ceil(len(a)/2)
    left, right = merge_sort(a[:x]), merge_sort(a[x:])
    return merge(left, right)

a = create_array()
print(a)
# a = [3,6,4]
# b = [2,5,3]
# print(merge(a, b))
print(merge_sort(a))
# for _ in range(10):
#     print(_)