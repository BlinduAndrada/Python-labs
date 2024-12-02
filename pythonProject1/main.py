# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def gcd(a,b):
   if a==0 :
       return b
   return gcd(b%a,a)


nr=input("Dati numerele:")
nr_list=nr.split()
l=[]

for nr in nr_list:
    l.append(int(nr))


x=l[0]
y=l[1]

result=gcd(x,y)

for i in range (2,len(l)):
    result=gcd(result,l[i])

print(result)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
