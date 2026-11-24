class Solution:
    def encode(self, strs: List[str]) -> str:
        # We prepend each word with len+a delimiter.
        encoded=""
        for string in strs : 
            length = len(string)
            encoded+= str(length)+"$"+string
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded=[]
        i=0 
        while i < len(s) :
            j = i 
            while s[j] != "$" : 
                j+=1
            length=int(s[i:j])
            start= j+1
            end = start + length
            decoded.append(s[start:end:])
            i = end
        return decoded