aList=[10,-1,6,3,-2,9]
def smallest(aList):
    mini=aList[0]
    for i in range(0,len(aList)-1):
        if aList[i]<mini:
            mini=aList[i]
            return mini
#aList=[10,-1,6,3,-2,9]
print(smallest(aList))
