class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num = sorted(numbers)
        for i in range(len(num)): 
            for j in range(len(num)): 
                if i != j: 
                    if num[i] + num [j] == target: 
                        return [i+1, j+1]