import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import os

# Getting and printing PID for evaluation script
# pid = os.getpid()
# print(str(pid))
# input("Evaluation script started?") # Waiting for input to signalize that evaluation script is running

mill = 1000000
tho = 1000

# Initializing matrices
A = np.random.rand(mill, tho)
B = np.random.rand(tho, mill)
C = np.random.rand(mill, 1)
D = np.zeros((mill, 1))

####### CODE FOR CDF PLOT ###########
# H,X1 = np.histogram( A, bins = 10)
# pdf = H / sum(H)
# cdf = np.cumsum(pdf)
# plt.plot(X1[1:], cdf, label="CDF")
# plt.xlabel("value")
# plt.ylabel("percentage")
# plt.title("Empirical CDF of matrix A")
# plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
# #plt.show()                        #use plt.show to show figure in output window
# plt.savefig('cdf.png', dpi=300)    #use plt.savefig to save figure to file
###### END OF CDF PLOT CODE ########

# Matrix multiplication
for i in range(0, mill, 1000):
    D[i:i+1000, ] = (A[i:i+1000, ] @ B) @ C  # I do the matrix multiplication in multiple slices to fit the data in memory

# D = (A @ B) @ C # straight forward way leads to running out of memory
# D = A @ (B @ C) # easy way to get it to work
