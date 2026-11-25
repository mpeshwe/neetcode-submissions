class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Find the minimum length
        minLen = min(len(s) for s in strs)
        for i in range(minLen) : 
            char = strs[0][i]

            for s in strs :
                if s[i] != char :
                    return s[:i]
        return strs[0][:minLen]