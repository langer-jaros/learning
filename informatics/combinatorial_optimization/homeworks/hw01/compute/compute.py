import ctypes
from ctypes import c_int, c_char_p, c_void_p, c_double
from datetime import datetime

clib = ctypes.cdll.LoadLibrary("./build/knapsack.so")
clib.solve.argtypes = [c_int, c_char_p, c_char_p]
clib.solve.restype = c_double

NUMBERS = [4, 10, 15, 20] # [4, 10, 15, 20, 22, 25, 27] # [4, 10, 15, 20, 22, 25, 27, 30, 32, 35, 37, 40]
CONFIG = [
    {
        "inst": "../data/nr/NR{n}_inst.dat",
        "resu": "../data/computed/nr_resu/bf_n_n{n}_resu_test.csv",
        "method": 0
    },
    {
        "inst": "../data/nr/NR{n}_inst.dat",
        "resu": "../data/computed/nr_resu/bab_n_n{n}_resu_test.csv",
        "method": 1,
    },
    {
        "inst": "../data/zr/ZR{n}_inst.dat",
        "resu": "../data/computed/zr_resu/bf_z_n{n}_resu_test.csv",
        "method": 0,
    },
    {
        "inst": "../data/zr/ZR{n}_inst.dat",
        "resu": "../data/computed/zr_resu/bab_z_n{n}_resu_test.csv",
        "method": 1,
    }
]

for conf in CONFIG:
    for n in NUMBERS:
        time = clib.solve(conf["method"], conf["inst"].format(n=n).encode(), conf["resu"].format(n=n).encode())
        print("n:", n, "current time:", datetime.now().strftime("%H:%M:%S"))
