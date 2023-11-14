Number = int(input())

for i in range(Number):
  print( " " * (Number - i-1)   + "*" * (i*2+1) )