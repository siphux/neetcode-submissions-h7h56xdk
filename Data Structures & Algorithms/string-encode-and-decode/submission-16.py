class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            length = len(word)
            if length < 10:
                length = "00" + str(length)
            elif length < 100:
                length = "0" + str(length)
            else:
                length = str(length)
            res += length
            res += word
        return res
    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        i = 0
        while(True):
            if i >= len(s):
                break
            print(i)
            len_word = int(s[i:i+3])
            
            i += 3
            word = s[i:i+len_word]
            res.append(word)
            print(res)
            i += len_word
        return res
