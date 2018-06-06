
import os
import sys

def solve(a0, a1, a2, b0, b1, b2):
    Alice = 0
    Bob = 0
    A = [a0, a1, a2]
    B = [b0, b1, b2]
    for i in range(3):
        if A[i] > B[i]:
            Alice += 1
        elif A[i] < B[i]:
            Bob += 1
        else:
            continue
    print(Alice,Bob)    



a0A1A2 = input().split()

a0 = int(a0A1A2[0])

a1 = int(a0A1A2[1])

a2 = int(a0A1A2[2])

b0B1B2 = input().split()

b0 = int(b0B1B2[0])

b1 = int(b0B1B2[1])

b2 = int(b0B1B2[2])

solve(a0, a1, a2, b0, b1, b2)
