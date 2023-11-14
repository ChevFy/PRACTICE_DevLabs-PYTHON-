
A = []

while len(A) < 5 :
    inputNumber = int(input())
    A.append(inputNumber)

A.sort()
A.reverse()

for i in A :
    print(i)