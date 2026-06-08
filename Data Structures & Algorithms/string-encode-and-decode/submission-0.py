class Solution:

    def encode(self, strs: List[str]) -> str:
        return ":;".join(strs) + ":;"

    def decode(self, s: str) -> List[str]:
        curr: str = ""
        result: list[str] = []
        count: int = 0

        while count < len(s):
            if s[count] == ":" and s[count + 1] == ";":
                result.append(curr)
                curr = ""
            elif s[count] != ";": 
                curr += s[count]

            count += 1            
        return result
            
            