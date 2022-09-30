from os import *
from sys import *
from collections import *
from math import *

def getInversions(arr, n):
	# Write your code here.
    count =  0
    for i in range(0, n-1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                count += 1
    return count

# Taking inpit using fast I/O.
def takeInput():
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = [3,2,1], 3 # output 3
print(getInversions(arr, n))