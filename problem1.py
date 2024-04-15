#! python3
 
"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is not frue

Enter a number: 36
36 is frue

Enter a number: 16
16 is not frue
"""


print("Enter a number")
x = input()
x = float(x)

y = x % 6
y = float(y)
yy = round(y,0)
yy = float(y)

z = x % 8 
z = float(z)
zz = round(z,0)
zz = float(zz)

if zz == z and yy == y:
    print("This number is divisible by 6 and 8")
    input()
if (yy == y == True):
    print("this number is divisible by 6")
    input()
if (zz == z == True):
    print("this number is divisible by 8")
    input()
else:
    print("this number is not divisible by 6 or 8")