class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {}
        for i , ch in enumerate(s):
            last[ch] = i

        seen = set()
        stack = []
        for i in range(len(s)):
            ch = s[i]
            if ch in seen:
                continue
            while stack and stack[-1] > ch and last[stack[-1]] > i:
                seen.remove(stack.pop())
            stack.append(ch)
            seen.add(ch)
        return ''.join(stack)    


                

        