import numpy

def simpson_varying(mypts,fun):
    x_left=mypts[0:-1]
    x_right=mypts[1:]
    x_mid=0.5*(x_left+x_right)
    dx=x_right-x_left

    y_left=fun(x_left)
    y_right=fun(x_right)
    y_mid=fun(x_mid)
    
    tot=numpy.sum(dx*(y_left+4*y_mid+y_right)/6.0)

    return tot

def myfun(x):
    y=1.0/(1+x**2)
    return y

if __name__=='__main__':
    x1=numpy.linspace(-10,-2,9)    
    x2=numpy.linspace(-1,1,21)
    x3=numpy.linspace(2,10,9)
    x=numpy.append(x1,x2)
    x=numpy.append(x,x3)
    
    myintegral=simpson_varying(x,myfun)
    pred=numpy.arctan(10)-numpy.arctan(-10)
    print myintegral, pred,myintegral-pred

