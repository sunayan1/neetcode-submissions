class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = []
        for i in range(len(temperatures)): 
            result.append(0)
            for j in range(i + 1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    result[i] = j - i
                    break
                else: 
                    continue 
        return result