Q1.
print("enter two numbers=")
num1 = float(input("num1="))
num2 = float(input("num2="))
add = num1 + num2
print("addition=",add)
sub = num1 - num2
print("subtraction=",sub)
mult = num1 * num2
print("multiplication=",mult)
div = num1 / num2
print("division=",div)
mod = num1 % num2
print("modulo=",mod)
power = num1 ** num2
print("power=",power)
floor = num1 // num2
print("floor=",floor)

Q2.
import math
print("enter length of three sides")
a = float(input("side1="))
b = float(input("side2="))
c = float(input("side3="))
s = ((a + b +c)/2)
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("area of triangle=",area)

Q3.
print("enter two numbers=")
a = float(input("num1="))
b = float(input("num2="))
if(a<=b or a>=b):
  if(a<=b):
    if(a<b):
      print("%d < %d" % (a,b))
    else:
      print("%d == %d" % (a,b))
  else:
    if(a>b):
      print("%d > %d" % (a,b))
    else:
      print("%d == %d" % (a,b))

Q4.
print("enter temperature in fahrenheit")
f = float(input("temperature="))
c = (f-32)*5/9
print("temperature in celsius= %f " % (c))

Q5.
import math
print"enter value in degree to find tan(x)"
a = float(input("value in degree="))
x = a*3.1415/180
y = math.tan(x)
print"tan(x)= %f" %(y)
print"enter value to find log(x)"
b = float(input("value="))
z = math.log(b)
print"log(x)=",z
print"enter value to find squareroot"
c = float(input("value="))
w = math.sqrt(c)
print"squareroot of x=",w

Q6.
print"enter radius of circle"
r = float(input("radius="))
perimeter = (2*3.1415*r)
area = (3.1415*r*r)
print"perimeter=",perimeter
print"area=",area

Q7.
import cmath
print"enter two complex numbers "
a = input("enter real part of first number=")
b = input("enter imaginary part of first number=")
z1 = complex(a,b)
c =input("enter real part of second number=")
d = input("enter imaginary part of second.
number=")
z2 = complex(c,d)
add = z1 + z2
print"addition=",add
sub = z1 - z2
print"subtraction=",sub

Q8.
a = input("num1=")
b = input("num2=")
c = a and b
d = a or b
e = not a
print"num1 and num2=",c
print"num1 or num2=",d
print"not num1=",e

Q9.
print"enter two numbers"
a = int(input("num1="))
b = int(input("num2="))
c = bin(a)
print"binary of num1=",c
d = bin(b)
print"binary of num2=",d
e, f, g = (a & b), (a | b), (a ^ b)
print"num1&num2=%d" % (e)
print"num1|num2= %d" % (f)
print"num1^num2=%d " % (g)
k = input("enter number to shift left=")
h = a << k
i = b << k
print"num1<<%d=%d" % (k, h)
print"num2<<%d=%d" % (k, i)
l = input("enter number to shift right=")
x = a >> l
y = b >> l
print"num1>>%d=%d" % (l, x)
print"num2>>%d=%d" % (l, y)

Q10.
print"enter two numbers"
a = input("first number=")
b = input("second number=")
temp = a
a = b
b = temp
print"first number after swap=",a
print"second number after swap=",b
