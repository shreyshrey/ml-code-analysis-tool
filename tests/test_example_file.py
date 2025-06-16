def test_check_for_duplicates_no_duplicates():
    #Test case 1:
    assert not check_for_duplicates([1, 2, 3, 4, 5])

def test_check_for_duplicates_with_duplicates():
    #Test case 2:
    assert check_for_duplicates([1, 2, 2, 3, 4])