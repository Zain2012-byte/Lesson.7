# python program to illustrate the use of 'is' identity operator

x=5

if (type(x) is int):
    print("true")
else:
    print("false")

x=0.5

if(type(x) is not float):
    print("true")
else:
    print("false")

x=20
y=20

if (x is y):
    print("x and y same identity")

y=30

if(x is not y):

    print("x and y have different identity")
    