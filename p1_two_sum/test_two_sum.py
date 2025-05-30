import pytest

from p1_two_sum.two_sum import Solution


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_two_sum(nums, target, expected):
    sol = Solution()
    assert sorted(sol.twoSum(nums, target)) == sorted(expected)


def test_two_sum_no_solution():
    sol = Solution()
    with pytest.raises(ValueError, match="No two sum solution"):
        sol.twoSum([1, 2, 3, 4], 100)
