global x
x = 50


def func(x):
    print('x is', x)
    x = 2
    print('change global x to', x)


func(x)
print('value of x is', x)
