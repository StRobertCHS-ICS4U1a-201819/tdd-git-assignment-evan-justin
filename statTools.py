#-------------------------------------------------------------------------------
# Name:	statTool.py
# Purpose:
# to create a single python module called statTools.py that contains functions
# for Measures of Central Tendency and Measures of Spread.
#
# Author:	Evan Bai / Justin Guo
#
# Created:	10/11/2018
#-------------------------------------------------------------------------------


# define a function mean()get the avg of a list of number
def mean(int_List):
   if int_List == []:
       return "The list is empty"
   else:
       total = 0
       for i in int_List:
           total += i
       avg = total/(len(int_List))
       return avg

# def a function median() to get the the middle item when the data are arranged from lowest to highest
def median(int_List):
   if int_List == []:
       return "The list is empty"
   else:
       int_List = sorted(int_List)
       if len(int_List) % 2 == 1:
           medIndex = len(int_List) // 2 + 1
           return int_List[medIndex - 1]
       else:
           medIndex1 = len(int_List) / 2
           medIndex2 = len(int_List) / 2 + 1
           return (int_List[medIndex1 - 1] + int_List[medIndex2 - 1]) / 2

# define a function mode() to get the observation that occurs most frequently in the list
def mode(int_List):
   int_List = sorted(int_List)
   count = 0
   num1 = 0
   num2 = 0
   if int_List == []:
       return "The list is empty"
   for i in int_List:
       volCount = int_List.count(i)
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
def Range(int_List):
   if int_List == []:
       return "The list is empty"
   else:
       return max(int_List) - min(int_List)