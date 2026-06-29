class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        for i in range(len(nums)): 
            temp = 1
            for j in range(len(nums)): 
                if j != i: 
                    temp = temp * nums[j]
            output[i] = temp
        return output