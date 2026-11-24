class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = dict()
        for string in strs : 
            key = "".join(sorted(string))
            if key in map : 
                map[key].append(string)
            else :
                map[key] = [string]
        ans = []
        for key,val in map.items() : 
            ans.append(val)
        return ans