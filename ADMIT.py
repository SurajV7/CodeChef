import sys, os, io

def main():
    # input = sys.stdin.readline
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    t = int(input())
    rankOfCollege = []
    rankOfStudent = []
    while t:
        t = t-1
        rankOfCollege.clear()
        rankOfStudent.clear()
        n, m = map(int, input().split())
        rankOfCollege = list(map(int, input().split()))
        rankOfStudent = list(map(int, input().split()))
        studentChoice = [[] for _ in range(m)]
        for i in range(m):
            studentChoice[i] = list(map(int, input().split()))
        colgObtained = [0 for _ in range(m)]
        colgAvailability = [1 for _ in range(n)]
        
        rankOfStudentNew = sorted(rankOfStudent)
        for s in range(m):
            if colgObtained[0] != 0:
                sys.stdout.write(str(colgObtained[0])+'\n')
                break
            else:
                nextTopRank = rankOfStudentNew[s]
                nextTopRankIndex = rankOfStudent.index(nextTopRank)
                rankOfStudent[nextTopRankIndex] = m+1

                numColgsApplied = studentChoice[nextTopRankIndex][0]
                for i in range(numColgsApplied):
                    nextColg = studentChoice[nextTopRankIndex][i+1]
                    if colgAvailability[nextColg-1] == 1:
                        colgObtained[nextTopRankIndex] = nextColg
                        colgAvailability[nextColg-1] = 0
            if colgObtained[0] != 0:
                sys.stdout.write(str(colgObtained[0])+'\n')
                break

        if colgObtained[0] == 0:
            sys.stdout.write(str(colgObtained[0])+'\n')



if __name__ == '__main__':
    main()