import numpy as np
from  mpi4py import MPI
import time
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


x = np.arange(0, 10000, 0.5)

n = len(x)
chunk = n // size

if rank != 0:
    x_rank = x[(rank *chunk) -1 : (rank+1)*chunk]
else:
    x_rank = x[(rank *chunk):(rank+1)*chunk]
# x_d = np.array_split(x , size)
#x_rank = x_d[rank]


t1 = time.time()
def num_int(x):
    y = (x)**5 + 3*x
    k = np.trapezoid(y, x) 
    time.sleep(x.size/10000)
    #print(f' solution of num_int is {k}' )
    return k
t2  = time.time()

if rank == 0: 
    add = 0
else:
    add = None

k = num_int(x_rank)
add = comm.reduce(k, op=MPI.SUM, root=0)

t2  = time.time()
print(f'time for mpi is {t2-t1}')
    #k = num_int(x)
    #add = np.sum(k)
if rank ==0:
    print(f'overall_sum of int is {add}' )

    t3= time.time()
    approx = num_int(x)
    print(f'num_int sol is{approx}')
    t4 = time.time()
    print(f'time for num is {t4-t3}')


