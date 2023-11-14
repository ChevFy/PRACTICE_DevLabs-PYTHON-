
cost = []
numberofgoods = int(input())

for i in range(numberofgoods) :
    inputcost = int(input())
    cost.append(inputcost)

print(sum(cost), "THB")