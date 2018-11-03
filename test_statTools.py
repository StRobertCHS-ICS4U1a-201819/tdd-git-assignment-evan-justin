from pytest import *
from statTools import *

# testing function mean
def test_mean_base1():
    assert(mean([1,2,3]) == 2)

def test_mean_base2():
    assert(mean([3,3,3,3]) == 3)

def test_mean_empty():
    assert(mean([]) == "The list is empty")

#testing function median()
def test_median_base1():
    assert(median([1,2,3]) == 2)

def test_median_base2():
    assert(median([1,3,2]) == 2)

def test_median_base3():
    assert(median([3,3,3]) == 3)

def test_median_empty():
    assert(median([]) == "The list is empty")