
import os
import sys

def staircase(n):
    pyramid = []
    for i in range(0,n):
        print((' ')*(n-i-1)+(i+1)*('#'))

if __name__ == '__main__':
    n = int(input())

    staircase(n)
