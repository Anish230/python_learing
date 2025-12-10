
# def fat():
#     n=int(input("Enter a number :"))
#     t=1
#     for i in range (1,1100):
#         t=t*i
#     if t==n:
#         return t 
# print(fat())


# def fact(n):
#     i=n
#     t=i*i-1
#     if t==n:
#         print(t)
#     else:
#         fact(i)

# n =int(input("Enter a number :"))        
# fact(n)      

# factorial function
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)

n = int(input("Enter a number: "))
print(fact(n))

# sum of n number
def total_sum(n):
    if n == 1:
        return 1
    else:
        return n +total_sum(n-1)
n = int(input("Enter a number :"))
print(total_sum(n))

# lambda function for addition

add = lambda x,y : x + y 
print("The addition is : ",add(5,6))