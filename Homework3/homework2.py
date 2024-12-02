#PROBLEMA 1
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

# nr=input("Dati numarul: ")
# print(fibo(int(nr)))

#PROBLEMA 2

def prim(x):
    if x<2:
        return 0
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

# nr=input("Dati numerele:")
# nr_list=nr.split()
# list=[]
#
# for nr in nr_list:
#     list.append(int(nr))
#
# print(prim_list(list))

#PROBLEMA 3




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

# list=input("Dati numerele pentru a:")
# nr_list=list.split()
# a=[]
# for i in nr_list:
#     a.append(int(i))
#
# list=input("Dati numerele pentru b:")
# nr_list=list.split()
# b=[]
# for i in nr_list:
#     b.append(int(i))
#
# print(multimi(a,b))

#PROBLEMA 4

def compose(notes, moves, start):
    song = []
    song.append(notes[start])
    for i in moves:
        if start+i<len(notes):
            start=start+i
        else:
            start=start+i-len(notes)
        song.append(notes[start])
    return song




# notes = ["do", "re", "mi", "fa", "sol"]
# moves = [1, -3, 4, 2]
# start = 2
# print(compose(notes, moves, start))


#PROBLEMA 5


def replace_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for row in range(rows):
        for col in range(cols):
            if row>col:
                matrix[row][col]=0

    return matrix

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
#
# new_matrix=replace_matrix(matrix)
#
# for row in new_matrix:
#     print(row)

#problema 6

def appears(x, *matrix):
    number = []
    for rows in matrix:
        for elem in rows:
            count = 0
            if elem not in number:
                for row in matrix:
                    count += row.count(elem)
                if count == x:
                    number.append(elem)
    return number

# x = 2
#
# print(appears(x,[1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]))
#
# # [1,2,3], [2,3,4],[4,5,6], [4,1, "test"]

#PROBLEMA 7

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

# list=[121,8998,423,908,233332]
# print(make_tuple(list))

#PROBLEMA 8
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


# print(ascii_list(["test", "hello", "lab002"],2,False))

#PROBLEMA 9

def check_view(matrix):
    rows = len(matrix)
    blocked_seats = []

    if rows == 0:
        return []

    cols = len(matrix[0])

    for col in range(cols):
        current_max_height = matrix[0][col]

        for row in range(1, rows):
            height = matrix[row][col]

            if height <= current_max_height:
                blocked_seats.append((row, col))
            else:
                current_max_height = height

    return blocked_seats

# matrix=[[1, 2, 3, 2, 1, 1],
#  [2, 4, 4, 3, 7, 2],
#  [5, 5, 2, 5, 6, 4],
#  [6, 6, 7, 6, 7, 5]]
# print(check_view(matrix))


#PROBLEMA 10


def tuples_maker(*args):
    max_length = max(len(lst) for lst in args)
    lengths = [len(l) for l in args]
    result = []
    for i in range(max_length):
        new_list = []
        for j, list in enumerate(args):
            if i >= lengths[j]:
                new_list.append(None)
            else:
                new_list.append(list[i])
        result.append(tuple(new_list))
    return result

# print(tuples_maker( [1,2,3,"a"], [5,6,7], ["a", "b", "c"]))

#PROBLEMA 11
def sort_tuples(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1][2])
#din curs

# tuples_list = [('abc', 'bcd'), ('abc', 'zza')]
# result = sort_tuples(tuples_list)
# print(result)

#PROBLEMA 12

def rhyme(words):
    rhyme_groups = []

    for word in words:
        if len(word) < 2:
            continue
        rhyme_key = word[-2:]
        ok = 0
        for group in rhyme_groups:
            if group[0][-2:] == rhyme_key:
                group.append(word)
                ok = 1
                break

        if not ok:
            rhyme_groups.append([word])

    return rhyme_groups


# print(rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))
