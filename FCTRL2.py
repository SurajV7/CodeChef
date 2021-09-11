import sys, io, os

def factorial(n):
    ans = 1
    if n>0:
        ans = n * factorial(n-1)
    return ans

input = sys.stdin.readline
t = int(input())
while t:
    n = int(input())
    t = t-1
    sys.stdout.write(str(factorial(n))+ '\n')
