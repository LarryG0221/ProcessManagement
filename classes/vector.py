


def outfun(num1):
    def innerfun(num2):
        return num2 * 10
    
    return innerfun(num1)

a= outfun(10)
print(a)


def  add(num1, num2):
    return num1+num2

def subs(num1, num2):
    return num1 -  num2


def cal(fun):
    n1, n2 = 10, 4
    rel = fun(n1,n2)
    return rel

print(cal(subs))