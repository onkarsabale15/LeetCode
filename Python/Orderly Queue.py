class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        N = len(s)
        if k == 1:
            res = s
            for i in range(1, N):
                newStr = s[i:] + s[0:i]
                if newStr < res:
                    res = newStr
            return res
        res = list(s)
        res.sort(key=ord)
        return "".join(res)