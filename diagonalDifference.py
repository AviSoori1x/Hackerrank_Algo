

import os
import sys
from math import sqrt

def diagonalDifference(a):
    sumlr = 0
    sumrl= 0
    n = len(a)
    for i in range(0,n):
        sumlr += a[i][i]
        sumrl += a[i][n-i-1]
    return abs(sumrl-sumlr)
    #or
    
      



n = int(input())

a = []

for _ in range(n):
    a.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(a)
print(result)
