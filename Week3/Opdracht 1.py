def check(a,i): # ga na of i aan a toegevoegd kan worden
    n = len(a)
    return not (i in a or i+n in [a[j]+j for j in range(n)] or i-n in [a[j]-j for j in range(n)])

def printQueens(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i] == j:
                print("X",end= " ")
            else:
                print("*",end= " ")
        print()
    print()

def rsearch(amountOfQueens, queenList):
    global solutionList
    for i in range(amountOfQueens):
        if check(queenList, i):
            queenList.append(i)
            if len(queenList) == amountOfQueens:
                solutionList.append(list(queenList))
                rsearch(amountOfQueens, queenList)
            else:
                if rsearch(amountOfQueens, queenList):
                    return True
            del queenList[-1] # verwijder laatste element
    return False

queenList = []
solutionList = [] # a geeft voor iedere rij de kolompositie aan
rsearch(8, queenList)
print(solutionList)

print("Amount of solutions:", len(solutionList))
printQueens(solutionList[0])