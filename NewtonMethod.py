from math import e
from math import log
def Newton_Method(p0,Tol=1e-5,N0=100):
    i=1
    while(i<=N0):
        p=p0-(f(p0))/fd(p0)
        if abs(p-p0)<Tol:
            return p
        i+=1
        p0=p
    return "msg fail"
#(a)
def f(x):
    return pow(x,3)-2*pow(x,2)-5

def fd(x):
    return 3*pow(x,2)-4*x

print(Newton_Method(3))  # ===> 2.690647448028614

# #(b)
# def f(x):
#     return pow(x,2)-2*x/(pow(e,x))+(1/pow(e,2*x))

# def fd(x):
#     return 2*(x+((x-1)/pow(e,x))-(1/(pow(e,2*x))))

# print(Newton_Method(1)) # ===> 0.5671490371724834

# #(c)

# def f(x):
#     return pow(x,3)-3*pow(x,2)*pow(2,-1*x)+3*x*pow(4,-1*x)-pow(8,-1*x)

# def fd(x):
#     return 3*pow(x,2)+3*((x**2)*pow(2,-1*x)*log(2)-2*x*pow(2,-1*x))-3*(x*pow(4,-1*x)*log(4)-pow(4,-1*x))+log(8)*pow(8,-1*x)

# print(Newton_Method(1)) # ===> 0.6411992303081061

