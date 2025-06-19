import pytest

def check_for_duplicates(input):
    return len(input) != len(set(input))

#Test case 1: No duplicates in the input
def test_check_for_duplicates_no_duplicates():
    assert not check_for_duplicates('abcdefg'), "Test case 1 failed"

#Test case 2: Duplicates exist in the input
def test_check_for_duplicates_with_duplicates():
    assert check_for_duplicates('abcdegf'), "Test case 2 failed"