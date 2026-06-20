from operator import itemgetter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = nums.count(num)

        values = [elem[0] for elem in sorted(freq.items(), key= itemgetter(1), reverse= True)]
        return values[:k]