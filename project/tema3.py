def my_function1(*args):
    suma = 0
    for arg in args:
        if isinstance(arg, int) or isinstance(arg, float):
            suma += arg
    return suma

print(my_function1(1,5,-3,'abc',[12,56,'cad']))
print(my_function1())
#print(my_function1(2, 4, 'abc', param_1=2))


def function2():
    try:
        number  = int(input())
    except ValueError:
        return 0
    else:
        return number


print(function2())





