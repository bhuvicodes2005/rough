def regulaFalsi(p0,p1,Tol=1e-6,N0=100):
    i=2
    q0=f(p0)
    q1=f(p1)
    while(i<=N0):
        p=p1-q1*((p1-p0)/(q1-q0))
        if abs(p-p1)<Tol:
            return p
        i+=1
        q=f(p)
        if(q*q1)<0:
            p0=p1
            q0=q1
        p1=p
        q1=q    

    return "msg fail"


def f(x):
    return 230*(x**4)+18*(x**3)+9*(x**2)-221*x-9

print(regulaFalsi(-1,0))  #-0.04065849904334182
print(regulaFalsi(0,1)) #0.9623983842387566