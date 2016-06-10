import numpy
from matplotlib import pyplot as plt
plt.ion()


samps=numpy.loadtxt('example_chain.txt')

#to look at convergence, we can plot the Fourier transform of the 
#chain samples.  If we see a bend with many points below it, we
#can be confident of convergence
#let's also just check one parameter for now.  You should check all of them if you're doing
#something yourself.
myfft=numpy.abs(numpy.fft.rfft(samps[:,0]))
myfft=numpy.abs(myfft)

plt.clf()

#don't plot the zeroth frequency - that is just the mean value of the parameters and isn't related to the scatter/convergence
freq=numpy.arange(1,myfft.size)
plt.plot(freq,myfft[1:],'.')

ax=plt.gca()
ax.set_yscale('log')
ax.set_xscale('log')

plt.savefig('chain_power_spectrum.png')
