def add(x,y):
    total = x + y
    return  "sum: "+ str(total)

def diff(x,y):
    ans = x - y
    return  "diff: "+ str(ans)
def pro(x,y):
    ans2 = x * y
    return  "product: "+ str(ans2)

def first(a=8,b=2,c=1):
    total = add(a,b)
    sub = diff(a,c)
    product = pro(b,c)
    answer = "The answers are "+ total + " " + sub + " " + product
    print(answer)

first()