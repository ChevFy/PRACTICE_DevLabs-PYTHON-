Year = int(input())

if Year == 1800 :
  print("Not a Leap Year")
elif (Year % 4) == 0 :
  print("Leap Year")
elif (Year % 4) != 0 :
 print("Not a Leap Year")