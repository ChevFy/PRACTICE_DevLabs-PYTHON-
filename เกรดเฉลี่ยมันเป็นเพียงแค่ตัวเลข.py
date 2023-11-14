Grade = []

while len(Grade) < 5  :
    a = float(input())
    Grade.append(a)


GPA = sum(Grade)/len(Grade)

print("THAI =" , Grade[0] )
print("MATH =" , Grade[1] )
print("ENGLISH =" , Grade[2] )
print("SCIENCE =" , Grade[3] )
print("SPORT =" , Grade[4] )
print("---")
print("GPA =" , GPA)
