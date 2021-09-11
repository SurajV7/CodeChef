import sys
t = int(input())
while t:
    t -= 1
    n = int(input())
    arr = list(map(int, input().split()))
    s1 = sys.maxsize
    s2 = sys.maxsize
    for i in range(n):
        if arr[i]<s1:
            s2 = s1
            s1 = arr[i]
        elif arr[i]<s2:
            s2 = arr[i]
    sum = s1+s2
    print(sum)