
def binary(x):
    x=bin(x).replace("0b","")
    count= x.count('1')
    return count

y=10
print(binary(y))