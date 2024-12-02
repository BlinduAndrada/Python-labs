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


x=1221
print(palindrom(x))