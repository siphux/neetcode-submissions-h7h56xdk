class Solution:
    def checkAnagram(self, s1: str, s2: str) -> bool:
        if len(s1) - len(s2) != 0:
            return False
        for l1, l2 in zip(sorted(s1), sorted(s2)):
            if l1 != l2:
                return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        was_checked = []
        for i in range(len(strs)):
            if strs[i] in was_checked:
                continue
            temp_res = [strs[i]]
            # print(f"first string {strs[i]}")
            for j in range(len(strs)):
                if i==j:
                    continue
                # print(f"second string {strs[j]}")
                if self.checkAnagram(strs[i], strs[j]):
                    temp_res.append(strs[j])
            res.append(temp_res)
            was_checked += temp_res
        return res

