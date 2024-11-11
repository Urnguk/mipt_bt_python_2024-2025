# # def func(x, y):
# #     print("function is called")
# #     print("function is finished")
# #     return x + y
# #
# #
# # z = func(5, 3)
#
#
# def prime(value):
#     if value < 2:
#         return False
#     for i in range(2, int(value ** 0.5) + 1):
#         if value % i == 0:
#             return False
#     return True
#
#
# for x in range(100):
#     if prime(x):
#         print(x)
#
# def foo(x):
#     print("this will be printed")
#     return
#     print("this won't be printed")
#
#
# foo(0)

# def bubble_sort(A):
#     for i in range(len(A) - 1):
#         for j in range(len(A) - 1 - i):
#             if A[j] >= A[j + 1]:
#                 A[j], A[j + 1] = A[j + 1], A[j]
#
#
# A = [2, 6, -8, 0, 2]
# bubble_sort(A)
# print(A)


x1= int(input())
y1=int(input())
x2= int(input())
y2=int(input())
x3= int(input())
y3=int(input())
def dist(x1,y1,x2,y2):
 x=(((x2-x1)**2)+((y2-y1)**2))**0.5
 return x
def per(x1,x2,y1,y2,x3,y3):
    a = dist(x1,y1,x2,y2)
    b = dist(x1,y1,x3,y3)
    c = dist(x3,y3,x2,y2)
    v =(a+b+c)/2
    return v
def sq(x1,x2,y1,y2,x3,y3):
    p = per(x1, x2, y1, y2, x3, y3)
    a = dist(x1, y1, x2, y2)
    b = dist(x1, y1, x3, y3)
    c = dist(x3, y3, x2, y2)
    n=(p*(p-a)*(p-b)*(p-c))**0.5
    return n

print(sq(x1,x2,y1,y2,x3,y3))
