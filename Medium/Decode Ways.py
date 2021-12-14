dict = {}

class Solution:
    def numDecodings(self, s: str) -> int:
        return self.helper(s)
        
    def helper(self, s):
        if len(s) == 0:
            return 1     
        if len(s) == 1:
            return 1 if s != '0' else 0
        else:
            if s in dict:
                return dict[s]
            greedy2 = 0
            greedy1 = 0
            if s[0] != '0':
                greedy1 = self.helper(s[1:])
            if int(s[:2]) <= 26 and s[0] != '0':
                greedy2 = self.helper(s[2:])
            dict[s] = greedy1 + greedy2
            return dict[s]