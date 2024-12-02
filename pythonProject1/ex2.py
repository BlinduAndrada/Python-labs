
vowels = ["a","e","i","o","u"]

count = 0

word="helloo"
for i in range(len(word)):
    if word[i] in vowels:
        count +=1

print(count)


