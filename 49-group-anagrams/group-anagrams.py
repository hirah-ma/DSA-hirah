from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            if ''.join(sorted(s)) not in d:
                d[''.join(sorted(s))].append(s)
            else:
                d[''.join(sorted(s))].append(s)


        result = []

        for i, v in  d.items():
            result.append(v)

        return result       



        