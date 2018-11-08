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

def Range(myList):
    if myList == []:
        return "The list is empty"
    else:
        return max(myList) - min(myList)

def mode(myList):
    myList = sorted(myList)
    count = 0
    num1 = 0
    num2 = 0
    if myList == []:
        return "The list is empty"
    for i in myList:
        volCount = myList.count(i)
        if volCount > count:
            count = volCount
            num1 = i
        elif volCount == count:
            num2 = i
    if num1 == num2:
        return num1
    else:
        return "no unique mode"

def lowerQuartile(myList):
    if myList == []:
        return "The list is empty"
    else:
        myList = sorted(myList)
        if len(myList) % 2 == 1:
            if (len(myList) - len(myList) // 2) % 2 == 1:
                medIndex = len(myList) // 2 + 1
                return myList[medIndex - 1]
            else:

        else:
            medIndex1 = len(myList)/2
            medIndex2 = len(myList)/2 + 1
            return (myList[medIndex1 - 1] + myList[medIndex2 - 1]) / 2