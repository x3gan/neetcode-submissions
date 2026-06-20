class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {"".join(sorted(ex)) : [] for ex in strs}
        print(words)
        for ex in strs:
            key = "".join(sorted(ex)) 
            if key in words.keys():
                words[key].append(ex)

        return list(words.values())