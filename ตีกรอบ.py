n = int(input())
a = n-2

print("#" * n)
for i in range(a) :
  print("#" + " "*(n-2) + "#")


if n != 1 :
  print("#" * n)
else :
  pass