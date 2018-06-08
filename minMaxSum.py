

import os
import sys

def miniMaxSum(arr):
    arr.sort()
    max = 0
    min = 0
    for i in range(1,5):
        max +=arr[i]
    for i in range(4):
        min +=arr[i]
    print(min,max)
 

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
