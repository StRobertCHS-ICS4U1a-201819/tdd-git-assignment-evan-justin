# define a function mean() to get the avg of a list of number
def mean(myList):
   if myList == []:
       return "The list is empty"
   else:
       total = 0
       for i in myList:
           total += i
       avg = total/(len(myList))
       return avg

# def a function median() to get the the middle item when the data are arranged from lowest to highest
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

# define a function mode() to get the observation that occurs most frequently in the list
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

# define a function Range() to get the difference between the largest and smallest result in the list
def Range(myList):
   if myList == []:
       return "The list is empty"
   else:
       return max(myList) - min(myList)



