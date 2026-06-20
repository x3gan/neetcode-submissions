class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for left in range(len(nums)):
            for right in range(left + 1, len(nums)):
                print(f"{left} {right}")
                if nums[left] + nums[right] == target:
                    return [left, right]