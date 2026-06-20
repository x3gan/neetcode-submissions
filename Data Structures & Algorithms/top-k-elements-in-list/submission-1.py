from operator import itemgetter
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        print(freq)
        values = [elem[0] for elem in sorted(freq.items(), key= itemgetter(1), reverse= True)]
        return values[:k]