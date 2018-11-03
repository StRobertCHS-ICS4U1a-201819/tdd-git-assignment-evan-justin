def mean(myList):
    if myList == []:
        return "The list is empty"
    else:
        total = 0
        for i in myList:
            total += i
        avg = total/(len(myList))
        return avg


def median(myList):
    if myList == []:
        return "The list is empty"
    else:
        myList = sorted(myList)
        if len(myList) % 2 == 1:
            medIndex = len(myList)//2 + 1
            return myList[medIndex - 1]
        else:
            medIndex1 = len(myList)/2
            medIndex2 = len(myList)/2 + 1
            return (myList[medIndex1 - 1] + myList[medIndex2 - 1]) / 2