import sys, os, io

def main():
    input = sys.stdin.readline
    t = int(input())
    while t:
        t = t-1
        n, m = map(int, input().split())
        rankOfCollege = list(map(int, input().split()))
        rankOfStudent = list(map(int, input().split()))
        studentChoice = [[] for _ in range(m)]
        for i in range(m):
            studentChoice[i] = list(map(int, input().split()))
        





if __name__ == '__main__':
    main()