import ctypes
from ctypes import c_char_p, c_void_p, c_double
from datetime import datetime

clib = ctypes.cdll.LoadLibrary("./build/knapsack.so")
clib.solve.argtypes = [c_char_p, c_char_p]
clib.solve.restype = c_double


NUMBERS = [4, 10, 15, 20, 22, 25, 27, 30, 32, 35, 37, 40] # [4, 10, 15, 20]

INSTANCES = "../data/zr/ZR{n}_inst.dat" # "../data/nr/NR{n}_inst.dat"
RESULTS = "../data/zr/res/Z{n}.csv"


for n in NUMBERS:
    time = clib.solve(INSTANCES.format(n=n).encode(), RESULTS.format(n=n).encode())
    print("n:", n, "current time:", datetime.now().strftime("%H:%M:%S"))
