class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {"".join(sorted(ex)) : [] for ex in strs}
        print(words)

        for ex in strs:

            if "".join(sorted(ex)) in words.keys():
                words["".join(sorted(ex))].append(ex)

        return list(words.values())