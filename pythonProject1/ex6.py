
def checkNumber(s):
    rez=0
    for i in range(len(s)):
        if s[i].isdigit():
            while s[i].isdigit():
                rez=rez*10+int(s[i])
                i+=1
            return rez

word="abc123abc345"
print(checkNumber(word))
