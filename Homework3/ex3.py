
#am considerat multimile a si b

def multimi(a,b):
    a_or_b=[]
    a_and_b=[]
    a_minus_b=[]
    b_minus_a=[]


# a intersected with b

    for i in a:
        ok=0
        for j in b:
            if i==j:
               ok=1
        if ok==1:
            a_and_b.append(i)

#a minus b
    for i in a:
        ok=1;
        for j in b:
            if i==j:
                ok=0
        if ok==1:
            a_minus_b.append(i)

#b minus a
    for i in b:
        ok=1;
        for j in a:
            if i==j:
                ok=0
        if ok==1:
            b_minus_a.append(i)

# a reunited with b
    a_or_b=a_and_b+a_minus_b+b_minus_a

    return (a_or_b,a_and_b,a_minus_b, b_minus_a)

list=input("Dati numerele pentru a:")
nr_list=list.split()
a=[]
for i in nr_list:
    a.append(int(i))

list=input("Dati numerele pentru b:")
nr_list=list.split()
b=[]
for i in nr_list:
    b.append(int(i))

print(multimi(a,b))