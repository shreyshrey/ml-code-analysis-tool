import pytest

def check_for_duplicates(input):
    return len(input) != len(set(input))

#Test case 1: No duplicates
def test_no_duplicates():
    assert not check_for_duplicates([1, 2, 3, 4, 5]), "Test case 1 failed"

#Test case 2: One duplicate
def test_one_duplicate():
    assert check_for_duplicates([1, 2, 3, 4, 4]), "Test case 2 failed"

#Test case 3: Multiple duplicates
def test_multiple_duplicates():
    assert check_for_duplicates([1, 2, 2, 3, 3, 3]), "Test case 3 failed"

#Test case 4: Empty list
def test_empty_list():
    assert not check_for_duplicates([]), "Test case 4 failed"

#Test case 5: Single element
def test_single_element():
    assert not check_for_duplicates([1]), "Test case 5 failed"