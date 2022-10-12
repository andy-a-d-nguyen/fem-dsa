from bubble_sort import bubble_sort


def test_bubble_sort():
    arr = [5, 34, 76, 2, 45, 7, 8]
    assert bubble_sort(arr) == [2, 5, 7, 8, 34, 45, 76]