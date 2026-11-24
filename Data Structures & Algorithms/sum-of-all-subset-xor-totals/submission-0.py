class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        

        def backtrack(index , current)  :
            if index == len(nums) :
                return current
            return backtrack(index+1 ,current^nums[index]) + backtrack(index+1, current)
        return backtrack(0,0)