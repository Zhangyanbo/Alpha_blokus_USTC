# ref: http://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.convolve2d.html
# scipy.signal.convolve2d(in1, in2, mode='full', boundary='fill', fillvalue=0)[source]
from scipy import signal

m0 = [  [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]

core = [[1, 0], [0, -1]]

print("When boundary filled by 0:")

ans = signal.convolve2d(m0, core, boundary='fill', mode='same', fillvalue = 0)

print(ans)

print("When boundary filled by 1:")

ans = signal.convolve2d(m0, core, boundary='fill', mode='same', fillvalue = 1)

print(ans)
