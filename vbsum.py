import os
import sys

def aVeryBigSum(n, ar):
    sum = 0
    for num in ar:
        sum += num
    return sum


n = int(input())

ar = list(map(int, input().rstrip().split()))

result = aVeryBigSum(n, ar)

print(result)
