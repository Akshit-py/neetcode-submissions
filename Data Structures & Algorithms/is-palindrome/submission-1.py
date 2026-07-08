import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        rs=re.sub('[^a-zA-Z0-9]','',s).lower()
        if rs==rs[::-1]:
            return True
        return False