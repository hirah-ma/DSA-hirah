class Solution:
    def firstUniqChar(self, s: str) -> list:
        h = {}
        for i in range(len(s)):
            if s[i] not in h:
                h[s[i]] = [i]
            elif s[i] in h:
                h[s[i]].append(i)
        r = []
        for x, y in h.items():
            if len(y) == 1:
                r.append(y[0])
        if not r:
            return -1
        return min(r)

        