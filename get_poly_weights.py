import numpy

def get_poly_weights(order):
    x=numpy.linspace(-1,1,order+1)

    mat=numpy.zeros([order+1,order+1])

    mat[:,0]=1
    for i in range(order):
        mat[:,i+1]=mat[:,i]*x

    #normally, we have to solve (A^T N^-1 A)p = A^T N^-1 d
    #to get fit parameters p from data points d.
    #however, in the case where A is square and invertible,
    #we can multiply through on the left and get
    #p=A^-1 d 
    mat_inv=numpy.linalg.inv(mat)

    #now we have p=mat_inv*d
    #think of mat_inv as a set of weights for each data point for each term
    #in the polynomial.  To find the area under the curve, we can find the area under
    #each polynomial and sum them.
    #the area under the nth polynomial from -1 to 1 is 2/(n+1) if n is even, 0 if n is odd
    area_weighted=mat_inv.copy()
    for i in range(0,order+1):
        if i%2==0:
            area_weighted[i,:] *= 2.0/(i+1)
        else:
            area_weighted[i,:]=0
    #total area is now the sum of the area under each polynomial
    weights=numpy.sum(area_weighted,axis=0)
    #of course, our interval was from -1 to 1, so if we want the average value,
    # we need to divide by 2 again
    weights /= 2.0
    return weights

if __name__=='__main__':
    
    for ord in numpy.arange(2,10,2):
        weights=get_poly_weights(ord)
        print ''
        print 'weights for order ' + repr(ord) + ' are ' + repr(weights)
