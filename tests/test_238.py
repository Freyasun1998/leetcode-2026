import pytest
from Array_String.LC_238 import Solution

@pytest.fixture
def solution():
    return Solution()

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3, 4], [24, 12, 8, 6]),
    ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ([0, 0], [0, 0]),
    ([0, 1], [1, 0]),
    ([1, 0], [0, 1]),
    ([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
    ([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
])
def test_product_except_self(solution, nums, expected):
    assert solution.productExceptSelf(nums) == expected