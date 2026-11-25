class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0
        read = 0
        while read < len(nums) :
            if nums[read] == val :
                read +=1
                continue
            nums[read],nums[write] = nums[write],nums[read] 
            write += 1
            read += 1
        return write