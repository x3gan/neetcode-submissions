class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = []
        for num in nums:
            a = nums.copy()
            a.remove(num)
            print(math.prod(a))
            prods.append(math.prod(a))

        return prods