class Solution:
    def isPalindrome(self, s: str) -> bool:
        sym = ".,:;@#-_[](){}/?!'/|\ `" + '"'
        s = ''.join([char for char in s if char not in sym]).lower()
        r = reversed(s)
        if list(s) == list(r):
            return True
        else:
            return False