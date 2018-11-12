#-------------------------------------------------------------------------------
# Name:    statTool.py
# Purpose:
# to create a single python module called statTools.py that contains functions
# for Measures of Central Tendency and Measures of Spread.
#
# Author:  Evan Bai / Justin Guo
#
# Created: 10/11/2018
#-------------------------------------------------------------------------------

import math
# define a function mean()get the avg of a list of number
def mean(int_List):
    """Find the average of the list

    :param int_List: list a set of data
    :return: float the mean of the list
    """
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
    """Find the median of the list

    :param int_List: list a set of data
    :return: float the median of the list
    """
    int_List = sorted(int_List)
    if int_List == []:
         return "The list is empty"
    else:
         int_List = sorted(int_List)
         if (len(int_List) + 1) % 2 != 0:
              medianIndex1 = (len(int_List) + 1) // 2
              medianIndex2 = (len(int_List) + 1) // 2 + 1
              return (int_List[medianIndex1 - 1] + int_List[medianIndex2 - 1]) / 2
         else:
              medianIndex = (len(int_List) + 1) // 2
              return int_List[medianIndex - 1]

# define a function mode() to get the observation that occurs most frequently in the list
def mode(int_List):
    """Find the mode of the list

        :param int_List: list a set of data
        :return: float the median of the mode
    """
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
    """Find the range of the list

        :param int_List: list a set of data
        :return: float the range of the list
    """
    if int_List == []:
         return "The list is empty"
    else:
         return max(int_List) - min(int_List)

# define a function lowerQuartile() to get the lower quartile of the list
def lowerQuartile(int_List):
    """Find the lower quartile of the list

        :param int_List: list a set of data
        :return: float the lower quartile of the list
    """
    int_List = sorted(int_List)
    if int_List == []:
         return "The list is empty"
    else:
         int_List = sorted(int_List)
         if (len(int_List) + 1) % 4 != 0:
               lowerQuartileIndex1 = (len(int_List) + 1) // 4
               lowerQuartileIndex2 = (len(int_List) + 1) // 4 + 1
               return (int_List[lowerQuartileIndex1 - 1] + int_List[lowerQuartileIndex2 - 1]) / 2
         else:
               lowerQuartileIndex = (len(int_List) + 1) // 4
               return int_List[lowerQuartileIndex - 1]

# define a function lowerQuartile() to get the upper quartile of the list
def upperQuartile(int_List):
    """Find the median of the list

        :param int_List: list a set of data
        :return: float the median of the list
    """
    int_List = sorted(int_List)
    if int_List == []:
          return "The list is empty"
    else:
          int_List = sorted(int_List)
          if (len(int_List) + 1) % 4 != 0:
               upperQuartileIndex1 = (len(int_List) + 1) * 3 // 4
               upperQuartileIndex2 = (len(int_List) + 1) * 3 // 4 + 1
               return (int_List[upperQuartileIndex1 - 1] + int_List[upperQuartileIndex2 - 1]) / 2
          else:
               upperQuartileIndex = (len(int_List) + 1) * 3 // 4
               return int_List[upperQuartileIndex - 1]


#define a function variance()to get the average of the squares of the differences of each number from the mean
def variance(int_List):
    """Find the variance of the list
    
        :param int_List: list of a set of number
        :return: variance of the list
    """
    avg = 0
    if int_List == []:
        return "The list is empty"
    else:
        total = 0
        number = 0
        for i in int_List:
            total += i
            number += 1
        mean = total / number
    for i in int_List:
        avg += (i - mean) ** 2
    return round(avg / len(int_List), 3)

def standard_deviation(int_List):
    """Find the standard deviation of the list
    
        :param int_List: list of a set of number
        :return: standard deviation of the list
    """
    avg = 0
    if int_List == []:
        return "The list is empty"
    else:
        total = 0
        number = 0
        for i in int_List:
            total += i
            number += 1
        mean = total / number
    for i in int_List:
        avg += (i - mean) ** 2
    variance = avg / len(int_List)
    return round(math.sqrt(variance))