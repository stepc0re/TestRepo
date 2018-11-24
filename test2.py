import numpy as np
from scipy.linalg import lstsq
import matplotlib.pyplot as plt

a = np.array([[1,2,5], [3,4,6]])
print(a.flatten('A'))

x = np.array([1, 2.5, 3.5, 4, 5, 7, 8.5])
y = np.array([0.3, 1.1, 1.5, 2.0, 3.2, 6.6, 8.6])


a = np.c_[np.array([1,2,3]), np.array([4,5,6]), np.array([7,8,9])]
print("a", a)