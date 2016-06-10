import numpy
def fit_exponential(x,order=5):

    #make a matrix filled with x^-n
    mat=numpy.zeros([x.size,order+1])
    mat[:,0]=1
    for i in range(0,order):
        mat[:,i+1]=mat[:,i]/x

    #make the y points because we don't have them passed in
    y=numpy.exp(x)    

    #do the usual least-squared fits
    lhs=numpy.dot(mat.transpose(),mat)
    rhs=numpy.dot(mat.transpose(),y)
    mat_inv=numpy.linalg.inv(lhs)
    fitp=numpy.dot(mat_inv,rhs)
    pred=numpy.dot(mat,fitp)


    return fitp,pred


if __name__=='__main__':
    x=numpy.linspace(1,5,1000)
    fitp,pred=fit_exponential(x,5)
    y=numpy.exp(x)
    print 'mean error for first fit is ' + repr(numpy.mean(numpy.abs(pred-y))) + ' with mean value ' + repr(numpy.mean(y))

