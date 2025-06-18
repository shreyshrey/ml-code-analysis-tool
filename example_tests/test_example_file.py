import pytest

def check_for_duplicates(input):
    return len(input) != len(set(input))

#Test case 1: Empty input
def test_check_for_duplicates_empty_input():
    assert not check_for_duplicates(""), "Empty string should not have duplicates"

#Test case 2: Single unique character
def test_check_for_duplicates_single_unique_character():
    assert not check_for_duplicates("a"), "Single unique character should not have duplicates"

#Test case 3: Repeated characters
def test_check_for_duplicates_repeated_characters():
    assert check_for_duplicates("aa"), "Repeated characters should have duplicates"

#Test case 4: Mixed characters with no duplicates
def test_check_for_duplicates_mixed_characters_no_duplicates():
    assert not check_for_duplicates("abc"), "Mixed characters without duplicates should not have duplicates"

#Test case 5: Mixed characters with duplicates
def test_check_for_duplicates_mixed_characters_with_duplicates():
    assert check_for_duplicates("abca"), "Mixed characters with duplicates should have duplicates"

#Test case 6: Long string with no duplicates
def test_check_for_duplicates_long_string_no_duplicates():
    assert not check_for_duplicates("abcdefghijklmnopqrstuvwxyz"), "Long string without duplicates should not have duplicates"

#Test case 7: Long string with duplicates
def test_check_for_duplicates_long_string_with_duplicates():
    long_string = "abcdefghijklmnopqrstuvwxyz" * 2 + "a"
    assert check_for_duplicates(long_string), "Long string with duplicates should have duplicates"