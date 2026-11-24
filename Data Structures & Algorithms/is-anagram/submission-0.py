class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        one = sorted(list(s))
        two = sorted(list(t))

        return one == two 