import numpy as np

def fft(x):
    n = len(x)
    if n == 1:
        return x

    n2 = n//2
    x1 = fft(x[0:n:2])
    x2 = fft(x[1:n:2])

    wn = np.exp(-1j*2*np.pi*np.arange(n2)/n)

    xout = np.zeros(n, dtype='complex')
    xout[0:n2] = x1 + wn*x2
    xout[n2:n] = x1 - wn*x2

    return xout