from numpy import *
from matplotlib import pyplot as plt

n=linspace(-40, 40, 81)
center=len(n)/2+1;
xyLim=5

f=0; N=50;
om=(2*pi)/N
ak_hist=[]
index=1
for k in range(0,4*N-1):

    ak=0;
    for i in range(int(-N/2), int(N/2)-1):
        if i>-N/4 and i<N/4:
            ak= ak+(1*exp(-1j*k*om*i));
        else:
            ak=ak+0;

    ak= (1/N)*sum(ak);
    ak_hist.append(ak)
    index=index+1

    if(k>N-1): continue;
    f= f+ak*exp(1j*k*om*n);

plt.plot(n, f)
plt.show()