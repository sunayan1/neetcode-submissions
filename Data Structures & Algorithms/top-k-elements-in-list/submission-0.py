class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums: 
            count[n] = 1 +count.get(n, 0) #in each iteration check the number exists in dictionary and count
        for n, c in count.items(): 
            freq[c].append(n) # append the iter no bucket if iteration number = freq of number

        res = []
        for i in range(len(freq)-1, 0, -1):  # go from end length of freq array to 1 ( 6 - 1)
            for n in freq[i]:  
                res.append(n)#if the iteration number got a  value, store in result
                if len(res) == k:  # if length of result equals k, return res
                    return res