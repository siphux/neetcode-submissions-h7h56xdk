class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dico_s, dico_t = {}, {}
        for letter in s:
            if letter not in dico_s:
                dico_s[letter] = 0
            dico_s[letter] += 1
        for letter in t:
            if letter not in dico_t:
                dico_t[letter] = 0
            dico_t[letter] += 1

        if dico_s == dico_t:
            return True
        return False