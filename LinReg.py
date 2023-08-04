# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 17:43:58 2023

@author: student
"""
import numpy as np
import numpy.linalg as lng


points = np.array([[1, 1], [3, 2], [3, 4], [6, 5], [7, 7]])

n = len(points)


A = []
for i in range(n):
    A.append([1, points[i][0]])
    
A = np.array(A)


b = []

for i in range(n):
    b.append(points[i][1])
    
b = np.array(b)
    
firstHalf = np.transpose(A) @ A


secondHalf = np.transpose(A) @ b


solution = lng.solve(firstHalf, secondHalf)

print(solution)


x = np.linspace(0, 10, 100)
y = solution[1] * x + solution[0] * np.ones(100)

from matplotlib import pyplot as plt

plt.plot(x, y)

for i in range(n):
    plt.scatter(points[i][0], points[i][1])
    
    
plt.show()





    
    