class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)-len(t) != 0 :
            return False
        dico_s = {}
        for letter in s:
            if letter not in dico_s:
                dico_s[letter] = 0
            dico_s[letter] += 1
        for letter in t:
            if letter in dico_s and dico_s[letter] > 0:
                dico_s[letter] -= 1

        if dico_s == {letter:0 for letter in s}:
            return True
        return False