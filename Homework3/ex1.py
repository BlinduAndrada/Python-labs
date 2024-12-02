# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def fibo(n):
    l=[]
    x=0
    y=1
    if n==0:
        return 0
    else:
        while n>0:
            l.append(x)
            sum=x+y
            x=y
            y=sum
            n-=1
    return l

nr=input("Dati numarul: ")
print(fibo(int(nr)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
