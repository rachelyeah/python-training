#用递归
def rabbit1(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rabbit1(n - 1) + rabbit1(n - 2)

# 用递归制作第二版
a = 0
rab = [0]*100


def rabbit2(n):
    global a
    a += 1
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        b = rabbit2(n - 1)
        rab[n - 1] = b
        c = rab[n - 2]
        return b + c


print(rabbit2(100), '{} : a'.format(a))


# a = 0
#
# def rabbit4(n, rab=[0]):
#     global a
#     a += 1
#     if n <= 0:
#         return rab[0]
#     elif n == 1:
#         rab.insert(1, 1)
#         return rab[1]
#     else:
#         b = rabbit4(n - 1)
#         rab.insert(n - 1, b)
#         c = rab[n - 2]
#         return b + c
#
#
# print(rabbit4(12), '{}: a'.format(a))
#
# def rabbit3(n):
#     global a
#     a += 1
#     print('{}: a'.format(a))
#
#     if n <= 0:
#         return rab.append(1)
#     elif n == 1:
#         return rab.append(1)
#     else:
#         if
#
#         b = rabbit3(n - 2)
#         c = rabbit3(n - 1)
#         return rabbit2(n - 1) + rabbit2(n - 2)
#
#
# def rabbit5(n):
#     if n <= 1 :
#         return 1
#     else:
#         a = rabbit5(n - 2)
#         b = rabbit5(n - 1)
#         c = rabbit5(a) + rabbit5(b)
#         a = b, b = c
#         return c
#
#
# #  用递归+列表制作
# def rabbit6(n) :
#     rab = []
#     if n <= 1:
#         return 1
#     else:
#         rab.append(1)
#         rab.append(1)
#         for i in range(2,n):
#             print('{}: '.format(i))
#             rab.append(rab[i - 1] + rab[i - 2])
#     return rab
#
#
# class Rabbit8:
#     def __init__(self, cap):
#         self.rab = [0] * cap
#         self.c = 0
#
#     def count(self, n):
#         self.c += 1
#         if n <= 0:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             if self.rab[n - 1] > 0:
#                 a = self.rab[n - 1]
#             else:
#                 a = self.count(n - 1)
#                 self.rab[n - 1] = a
#             if self.rab[n - 2] > 0:
#                 b = self.rab[n - 2]
#             else:
#                 b = self.count(n - 2)
#                 self.rab[n - 2] = b
#             return a + b
#
#
# # 修改后的class
# class Rabbit7:
#     def __init__(self, cap):
#         self.rab = [0] * cap
#         self.c = 0
#
#     def count(self, n):
#         self.c += 1
#         if n <= 0:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             a = self.count(n - 1)
#             self.rab[n - 1] = a
#             b = self.rab[n - 2]
#             return a + b
#
# print('Pls print a number 1')
# print(rabbit6(12))
# print('Pls print a number 2')
# print(Rabbit8(12))
# print('Pls print a number Class')
# r = Rabbit7(100)
# print(r.count(13), r.c, r.rab)
#
# #用循环制作
#
# def rabbit9(n):
#     i = 2
#     x1 = 0
#     x2 = 1
#     x3 = 0
#     a = [1]
#     if n >= 2:
#         while i < n + 1:
#             x3 = x1 + x2
#             x1 = x2
#             x2 = x3
#             i += 1
#             a.append(x3)
#         else:
#             return a
#     else:
#         return a
#
#
# d = rabbit9(8)
# print(d)
#
#
#
# d = rabbit9(1)
# print(d)


#     fib = [1, 1]
#     while i < n and n > 2:
#         a += fib[i - 1]
#         # a += fib[i]
#         fib = fib.append(a)
#         i = i + 1
#         if i == n - 1:
#             return fib
#         else:
#             continue
#     else:
#         if n == 1:
#             fib = [1]
#             return fib
#         else:
#             fib = [1, 1]
#             return fib
#
#
#
# print(rabbit2(6))
#     while n > 1:
#         fib = [1, 1]
#         for i in range(2, n + 1):
#             abc = fib[i - 1] + fib[i - 2]
#             fib.append(abc)
#             return fib
#     return 1
#
# rab = [1, 2, 3, 4, 5, 6]
# c = rab
# print(c)