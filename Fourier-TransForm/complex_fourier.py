# 복소푸리에 급수를 이용하여 사각파 표현
from matplotlib import pyplot as plt
from numpy import *

x = linspace(-10, 10, 1000)
f = 0
N = 10000
for n in range(-N, N):
    # n값은 홀수여야만 실행하도록 구현
    if mod(n, 2) == 0 or n == 0:
        continue
    cn = 2 / (1j * n * pi)
    f = f + cn * exp(1j * n * x)

plt.plot(x, f)
plt.show()
