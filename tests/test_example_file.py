import pytest

def check_for_duplicates(input):
    return len(input) != len(set(input))

# Test case 1: Empty string should not have duplicates
def test_empty_string():
    assert not check_for_duplicates(""), "#Test case 1:"


# Test case 2: Single unique character should not have duplicates
def test_single_unique_char():
    assert not check_for_duplicates("a"), "#Test case 2:"


# Test case 3: String with no duplicates should return False
def test_no_duplicates():
    assert not check_for_duplicates("abcdefg"), "#Test case 3:"


# Test case 4: String with one duplicate character should return True
def test_one_duplicate_char():
    assert check_for_duplicates("abcdea"), "#Test case 4:"


# Test case 5: String with multiple duplicate characters should return True
def test_multiple_duplicates_chars():
    assert check_for_duplicates("aabbccdd"), "#Test case 5:"