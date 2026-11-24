class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        L = 0 
        R = len(heights) - 1

        while L < R : 
            # which one's shorter ? 
            h = min(heights[L], heights[R]) 
            water = h * (R - L)
            ans = max(ans,water)

            if heights[L] == h :
                L+=1
            else :
                R -= 1
        return ans