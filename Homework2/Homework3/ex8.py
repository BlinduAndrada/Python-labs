def ascii_list(list,x=1,flag=True):
    result=[]
    for words in list:
        chars=[]
        for char in words:
            ascii_code=ord(char)
            if flag==1:
                if ascii_code%x==0:
                    chars.append(char)
            else:
                if ascii_code%x!=0:
                    chars.append(char)
        result.append(chars)
    return tuple(result)

#x = 2, ["test", "hello", "lab002"], flag = False
print(ascii_list(["test", "hello", "lab002"],2,False))