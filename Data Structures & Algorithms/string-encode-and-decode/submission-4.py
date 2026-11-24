class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs : 
            ans += str(len(s)) + "#"
            ans+= s
        return ans
    def decode(self, s: str) -> List[str]:

        ans = []
        L = 0 

        while L < len(s) :
            R = L
            while s[R] != "#" :
                R +=1
            length = int(s[L:R])

            start = R+1
            stop = start + length
            ans.append(s[start:stop])

            L = stop
        return ans