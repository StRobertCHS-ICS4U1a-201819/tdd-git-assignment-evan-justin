#-------------------------------------------------------------------------------
# Name:	test_statTool.py
# Purpose:
# to test every single function in python module statTools.py
#
# Author:	Evan Bai / Justin Guo
#
# Created:	10/11/2018
#-------------------------------------------------------------------------------


from pytest import *
from statTools import *

# testing of central Tendency
# testing function mean
def test_mean_base1():
    assert(mean([1,2,3]) == 2)

def test_mean_base2():
    assert(mean([3,3,3,3]) == 3)

def test_mean_base3():
    assert(mean([1,2,3,4]) == 2.5)

def test_mean_base4():
    assert(mean([-4,-3,-2,-1,0,1,2,3,4]) == 0)

def test_mean_base5():
    assert(mean([0]) == 0)

def test_mean_empty():
    assert(mean([]) == "The list is empty")

# testing function median()
def test_median_base1():
    assert(median([1,2,3]) == 2)

def test_median_base2():
    assert(median([1,3,2]) == 2)

def test_median_base3():
    assert(median([3,3,3]) == 3)

def test_median_base4():
    assert(median([1,2,4,5]) == 3)

def test_median_base5():
    assert(median([0]) == 0)

def test_median_empty():
    assert(median([]) == "The list is empty")

# testing function mode()
def test_mode_base1():
    assert(mode([1,1,1,2,2,3]) == 1)

def test_mode_base2():
    assert (mode([1,2,3,1,2,1]) == 1)

def test_mode_empty():
    assert (mode([]) == "The list is empty")

def test_mode_noUniqueMode():
    assert (mode([1,1,1,2,2,2,3]) == "no unique mode")


# testing the Measures of Spread
# testing the function range()
def test_range_base1():
    assert(Range([1,2,3,4,5]) == 4)

def test_range_base2():
    assert(Range([1,3,5,2,4,6,4]) == 5)

def test_range_base3():
    assert(Range([1,1,1,1,1]) == 0)

def test_range_empty():
    assert(Range([]) == "The list is empty")

# testing the function upperQuartile
def test_upperQuartile_base1():
    assert(upperQuartile([1,2,3,4]) == 3.5)

def test_upperQuartile_base2():
    assert(upperQuartile([18,20,23,20,23,27,24,23,29]) == 25.5)

def test_upperQuartile_base3():
    assert(upperQuartile([1,2,3]) == 3)

def test_upperQuartile_empty():
    assert(upperQuartile([]) == "The list is empty")

