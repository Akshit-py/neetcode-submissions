from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        c1 = Counter(t)
        c2 = Counter()
        have, need = 0, len(c1)
        res = ""
        k = 0

        for j in range(len(s)):
            c2[s[j]] += 1
            if c2[s[j]] == c1[s[j]]:
                have += 1

            while have == need:
                window = s[k:j+1]
                if not res or len(window) < len(res):
                    res = window
                c2[s[k]] -= 1
                if c2[s[k]] < c1[s[k]]:
                    have -= 1
                k += 1

        return res