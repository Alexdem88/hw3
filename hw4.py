# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.
def nums():
    x = abs(int(input('x')))
    y= abs(int(input('y')))
    z = (x**y)
    print(z)
    return
nums()


