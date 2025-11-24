# Solution 1: standard check using !=
class Solution1:
    def duplicate_check(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


# Solution 2: alternative approach using >
class Solution2:
    def duplicate_check(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))


# ===============================
# Example usage for a project
# ===============================

from typing import List
nums1 = [1, 2, 3, 1, 5, 3]  # contains duplicates
nums2 = [1, 2, 3, 4, 8, 9, 6, 7]  # all unique

sol1 = Solution1()
sol2 = Solution2()

# Test nums1
print(sol1.duplicate_check(nums1))  # True
print(sol2.duplicate_check(nums1))  # True

# Test nums2
print(sol1.duplicate_check(nums2))  # False
print(sol2.duplicate_check(nums2))  # False

