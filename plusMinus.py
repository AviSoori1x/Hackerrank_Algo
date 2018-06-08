
import os
import sys

def plusMinus(arr):

    pnz = [0,0,0]
    totn =len(arr)
    for i in arr:
        if i >0:
            pnz[0] +=1
        elif i < 0:
            pnz[1] +=1
        else: 
            pnz[2] +=1
    for i in range(3):
        print(pnz[i]/totn)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
