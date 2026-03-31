class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_insensitive = [char.lower() for char in s if char.isalnum()]
        s_insensitive = "".join(s_insensitive)
        
        if len(s_insensitive) == 0:
            return True
        
        i, j = 0, len(s_insensitive)-1
        while i < j:
            if s_insensitive[i] != s_insensitive[j]:
                return False
            i +=1
            j -=1
        return True