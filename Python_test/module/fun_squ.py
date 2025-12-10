import math
def square(num):
  return (num*num)
print (square(8))

def multiply(a,b):
  return (a*b)
print (multiply(4,5))

def area_of_circle(r ):
    return (math.pi*r*r)
r=float(input ("Enter the value of r :"))
print (area_of_circle(r))

def maxmimun(x,y):
   if x>y:
         return x
   else:
         return y
   
print ("maxmimun is:", maxmimun(10,20)) 

def  greet(name="Student"):
    print ("Hello", name)
name = input("Enter your name: ")
greet(name)

def power(number, power=2):
    return (number**power)
print(power(2,2))

