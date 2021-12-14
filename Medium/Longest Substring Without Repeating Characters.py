

def lengthOfLongestSubstring(self, s: str) -> int:
        
        dict = {}
        rangeStart = 0
        max = 0
        for i in range(len(s)):
            if (s[i] not in dict) or (dict[s[i]] < rangeStart):
                dict[s[i]] = i
            else:
                curRange = i - rangeStart
                if curRange > max:
                    max = curRange
                rangeStart = dict[s[i]] + 1
                dict[s[i]] = i
        if len(s) - rangeStart > max:
            max = len(s) - rangeStart
            
        return max
                