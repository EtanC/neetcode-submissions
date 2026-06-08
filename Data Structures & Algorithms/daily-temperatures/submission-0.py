class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # bbrute force 
        result: list[int] = []
        for i in range(len(temperatures)):
            flagged: bool = False
            for j in range(i, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    result.append(j - i)
                    flagged = True
                    break
            if not flagged: 
                result.append(0)
        return result
                