
word = str(input())

revese = word.split()[::-1]
list = []

for i in revese :
    list.append(i)

print(" ".join(list))