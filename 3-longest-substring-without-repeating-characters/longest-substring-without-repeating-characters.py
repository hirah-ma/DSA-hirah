class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        h = {}
        i, j = 0, 0
        maxi = 0

        while j < len(s):
            if s[j] in h and h[s[j]] >= i:
                i = h[s[j]] + 1

            h[s[j]] = j
            maxi = max(maxi, j - i + 1)
            j += 1
        return maxi                      



        