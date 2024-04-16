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
import math
print("Enter a number")
x = input()
x = float(x)

y = x % 6
z = x % 8 

if y == 0 and z == 0:
    print("This number is divisible by 6 and 8")
    input()
if (y == 0):
    print("this number is divisible by 6")
    input()
if (z == 0):
    print("this number is divisible by 8")
    input()
else:
    print("this number is not divisible by 6 or 8")
    input()
