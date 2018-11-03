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
        if len(myList) % 2 == 1:
            medIndex = len(myList)//2 + 1