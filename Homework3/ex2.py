
def prim(x):
    for i in range(2,x//2 + 1):
        if x%i==0:
            return 0
    return 1


def prim_list(l):
    l1=[]
    for i in l:
        if prim(i)==1:
            l1.append(i)

    return l1

nr=input("Dati numerele:")
nr_list=nr.split()
list=[]

for nr in nr_list:
    list.append(int(nr))

print(prim_list(list))