#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    arr = list(s)
    hours = int(arr[0])*10+int(arr[1])
    minutes = int(arr[3])*10+int(arr[4])
    seconds = int(arr[6])*10+int(arr[7])
    if arr[8]== 'P' and hours != 12:
        hours = hours +12
    #if hours == 24:
    #    hours = '00'
    if hours==12 and arr[8] =='A':
        hours = '00'
    elif int(hours) < 10:
        hours = '0'+str(int(hours))
    if minutes < 10:
        minutes = '0'+str(minutes)
    if seconds < 10:
        seconds = '0'+str(seconds)
    return str(hours) +':'+ str(minutes) +':'+ str(seconds)
        

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result)
