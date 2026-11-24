class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums is an array of integers
        # return the length of longest consecutive 
        

        # make a set of all numbers
        set_ = set(nums) 
        max_ = 0
        for n in nums : 
            length = 0 
            if n-1 not in set_ :
                current = n 
                while current in set_ : 
                    current += 1
                    length += 1 

            if max_ < length : 
                max_ = length 
        return max_