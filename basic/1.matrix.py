import numpy as np
import pandas as pd
A = np.array([[1, 2], [1, 1]])
print(A)
A @ A # 矩阵乘法
B = np.arange(8).reshape(2, 4)
print(B.T) # transpose
E = np.eye(3)
print(E) #单位矩阵

D = np.arange(5)
diagnose = np.diag(D)
print(diagnose) # 对角矩阵
print(np.triu(A),'\n', np.tril(A)) # 取上三角,下三角


