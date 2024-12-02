def palindrom(n):
    x=n
    rev=0
    while n>0:
         rev=(rev*10)+n%10
         n=n//10

    if x==rev:
        return 1
    else:
        return 0


def make_tuple(list):
    l=[]
    max=0
    count=0
    for i in list:
        if palindrom(i)==1:
            count+=1
            if i>max:
                max=i
    l.append(count)
    l.append(max)
    y=tuple(l)
    return y

list=[121,8998,423,908,233332]
print(make_tuple(list))