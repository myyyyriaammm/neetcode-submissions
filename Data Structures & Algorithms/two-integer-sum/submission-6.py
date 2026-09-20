class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            nbr = target - n
            if nbr in d :
                return [d[nbr], i]
            d[n] = i 
        return          
        