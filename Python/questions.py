'''
=======================================================================
WAP to Calculate electricity bill based on given information(diff lab and rate per unit in each slab.)
read two values currentmonthreading and previousmonthreading & compute no of units
currentMonth = int(input("Enter Current Month Reading: "))
previousMonth = int(input("Enter Previous Month Reading: "))
unit = currentMonth-previousMonth
if unit>=1 and unit<=100:
    bill = int(unit*2)+10
    print(f"you bill is {bill}")
elif unit>=101 and unit<=250:
    bill = int(unit*3)+20
    print(f"you bill is {bill}")
elif unit>=251 and unit<=500:
    bill = int(unit*4)+30
    print(f"you bill is {bill}")
elif unit>=501 and unit<=1000:
    bill = int(unit*5)+40
    print(f"you bill is {bill}")
else :
    bill = int(unit*7)+50
    print(f"you bill is {bill}")
=======================================================================
# Train Berth Problem
n =int(input())
seatvalue =(n%8)
if(seatvalue == 1 or seatvalue == 4):
    print("LB")
elif(seatvalue == 2 or seatvalue == 5):
    print("MB")
elif(seatvalue == 3 or seatvalue == 6):
    print("UB")
else :
    if(seatvalue == 7):
        print("SLB")
    else :
        print("SUB")
=======================================================================
# Triangle problem
x= input("X: ")
y= input("Y: ")
z= input("Z: ")
if x == y == z:
    print("Equilateral")
elif x==y or y==z or z==x:
    print("isosceles")
else:
    print("Scalene triangle")
=======================================================================
# print Length of integer
a = [int(i) for i in input()]
print(len(a)) # Method 1
# Method 2
N=int(input())
if N in range(0,10):
    print("One Digit")
elif N in range(10,100):
    print("Two Digit")
elif N in range(100,1000):
    print("three Digit")
else:
    print("Something else")
=======================================================================
# Check whether a Char is Uppercase, Lowercase, number or a Special Character
a=input()
if ord(a) in range(65,91):
    print(f"{a} is a Uppercase")
elif ord(a) in range(97,123):
    print(f"{a} is a lowercase")
elif ord(a) in range(48,58):
    print(f"{a} is a Number")
else:
    print(f"{a} is a special Character")
=======================================================================
# WAP to Calculate Dog Years 1) for first 2 y is equivalent to 10.5, 2) after that 1y = 4
n=int(input("Enter the dog year: "))
if n<=2:
    print("Dog year is: ",n*10.5)
elif n>2:
    year=(n-2)*4+21
    print(f"Dog year is: {year}")
# Method 2
n = int(input())
print(((n-2)*4 + 2*10.5) if n>=2 else(n*10.5))
=======================================================================
# WAP to print %age of vowels in a string
b=[]
a=input()
for i in a:
    if i in "AEIOUaeiou":
        b.append(i)
c=(len(b)/len(a))*100
print(f"{c}%")
=======================================================================
# WAP that returns TRUE if the binary string can be rearranged to alternate 01 strings else FALSE
n=input()
a=[]
b=[]
for i in n:
    if i==0:
        a.append(i)
    elif i==1:
        b.append(i)
if len(a)%2==0 and len(b)%2==0:
    print("yes")
else:
    print("No")
# Method 2
s = input()
ctzero,ctone = 0,0
for i in s:
    if i == '0':
        ctzero += 1
    else:
        ctone += 1
if ctzero == ctone or ctzero - 1 == ctone or ctone - 1 == ctzero:
    print("yes")
else:
    print("no")
=======================================================================
'''
