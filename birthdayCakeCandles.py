
import os
import sys

def birthdayCakeCandles(n, ar):
    ar.sort()
    max = ar[n-1]
    num = 0
    for i in ar:
        if i==max:
           num +=1
    return num
        


n = int(input())

ar = list(map(int, input().rstrip().split()))

result = birthdayCakeCandles(n, ar)

print(result)
