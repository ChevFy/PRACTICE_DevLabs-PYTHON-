
N = int(input())
A = []

for h in range(N) :
    inputNumber = int(input())
    A.append(inputNumber)

A.sort()
A.reverse()

for i in A :
    print(i)