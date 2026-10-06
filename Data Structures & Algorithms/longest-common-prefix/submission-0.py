class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        len_strs = [len(str) for str in strs]
        smallest_size = min(len_strs)
        for i in range(smallest_size):
            current_elem = strs[0][i]
            for j in range(1, len(strs)):
                if current_elem != strs[j][i]:
                    return res
            res = res + current_elem
        return res

        