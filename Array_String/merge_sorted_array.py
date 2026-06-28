'''
You are given two integer arrays nums1 and nums2, 
sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in 
non-decreasing order.

The final sorted array should not be returned by the function, 
but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, 
where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. 
nums2 has a length of n.
'''
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        nums1[:p2 + 1] = nums2[:p2 + 1]


def test_merge_normal() -> None:
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    Solution().merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]


def test_merge_nums2_empty() -> None:
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2: List[int] = []
    Solution().merge(nums1, 3, nums2, 0)
    assert nums1 == [1, 2, 3, 0, 0, 0]


def test_merge_nums1_valid_portion_empty() -> None:
    nums1 = [0, 0, 0]
    nums2 = [1, 2, 3]
    Solution().merge(nums1, 0, nums2, 3)
    assert nums1 == [1, 2, 3]


def test_merge_duplicate_values() -> None:
    nums1 = [1, 2, 2, 0, 0]
    nums2 = [2, 3]
    Solution().merge(nums1, 3, nums2, 2)
    assert nums1 == [1, 2, 2, 2, 3]


def test_merge_single_element_arrays() -> None:
    nums1 = [2, 0]
    nums2 = [1]
    Solution().merge(nums1, 1, nums2, 1)
    assert nums1 == [1, 2]