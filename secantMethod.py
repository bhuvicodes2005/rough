def secantMethod(p0,p1,Tol=1e-6,N0=100):
    i=2
    q0=f(p0)
    q1=f(p1)
    while(i<=N0):
        p=p1-q1*((p1-p0)/(q1-q0))
        if abs(p-p1)<Tol:
            return p
        i+=1
        p0=p1
        p1=p
        q0=q1
        q1=f(p)
    return "msg fail"

def f(x):
    return 230*(x**4)+18*(x**3)+9*(x**2)-221*x-9

print(secantMethod(-1,0))  #-0.040659288315725135
print(secantMethod(0,1))  #-0.04065928831557162


