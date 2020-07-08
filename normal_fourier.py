# 일반푸리에급수를 이용하여 사각파 표현

from matplotlib import pyplot as plt
from numpy import *
f=0; a0=0
an=0; N=10
xyLim=pi;
x=linspace(-10,10,1000);

for n in range(1,N):
    bn=(2/pi)*(1-cos(n*pi))/n;
    f=f+a0+an*cos(n*x)+bn*sin(n*x);

plt.plot(x,f)
plt.show()