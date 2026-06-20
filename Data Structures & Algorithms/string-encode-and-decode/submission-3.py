class Solution:

    def encode(self, strs: List[str]) -> str:
        print("~".join(strs))
        return "~".join(strs) if strs else "null"

    def decode(self, s: str) -> List[str]:
        print(s)
        return s.split("~") if s != "null" else []