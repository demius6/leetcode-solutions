class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list = s.split(' ')
        i = 0
        while i != len(list):
            if list[i] == '':
                list.remove(list[i])
            else:
                i += 1
                continue
        return len(list[-1])
