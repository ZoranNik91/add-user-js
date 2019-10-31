# def create_array(size = 10, max = 50):
#     from random import randint
#     return [randint(0,max) for _ in range(size)]

# def merge(a, b):
#     c = []
#     a_idx, b_idx = 0, 0
#     while a_idx < len(a) and b_idx < len(b):
#         if a[a_idx] < b[b_idx]:
#             c.append(a[a_idx])
#             a_idx += 1
#         else:
#             c.append(b[b_idx])
#             b_idx += 1
#     if a_idx == len(a): c.extend(b[b_idx:])
#     else:               c.extend(a[a_idx:])
#     return c

# def merge_sort(a):
#     if len(a) <= 1: return a
#     left, right = merge_sort(a[:len(a)/2]), merge_sort(a[len(a)/2:])
#     return merge(left, right)

# # a = create_array()
# # print(a)
# a = [3,6,4]
# b = [2,5,3]
# print(merge(a, b))
# print(merge_sort([3,8, 1, 3]))
import math 
a = [1,2,3,4,5,6]
print(math.ceil(a[:3.3]))

# x =  math.ceil(n/2)
# y = n - x