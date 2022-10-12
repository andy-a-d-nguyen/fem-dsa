from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    for i in range(len(arr)):
        # Option 1 for looping
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

        # Option 2 for looping
        # for j in range(len(arr) - 1 - i):
        #     if arr[j] > arr[j + 1]:
        #         arr[j], arr[j + 1] = arr[j + 1], arr[j]
        #         # temp = arr[j]
        #         # arr[j] = arr[j + 1]
        #         # arr[j + 1] = temp
    return arr
