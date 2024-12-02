sir1="HelloWorldA"
sir2=""

for i in sir1:
    if(i.isupper()):
        sir2+="_"+i.lower()
    else:
        sir2+=i

print(sir2[1:])