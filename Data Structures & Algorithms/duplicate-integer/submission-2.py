nums = [1, 2, 3, 3]

# class Solution: 
#     def hasDuplicate(self, nums)->bool: 
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)) : 
#                 if nums[i] == nums[j]:
#                     return True     
#         return False

# solution = Solution()
# output = solution.hasDuplicate(nums)

class Solution: 
    def hasDuplicate(self, nums)->bool: 
        seen = set()
        for i in nums: 
            if i in seen: 
                return True
            else: 
                seen.add(i)
        return False

solution = Solution()
output = solution.hasDuplicate(nums)