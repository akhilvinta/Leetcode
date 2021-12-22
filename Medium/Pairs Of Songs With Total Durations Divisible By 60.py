class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hash = {}
        for a in time:
            hash[a%60] = 0

        count = 0
        for i,a in enumerate(time):
            complement = 0 if (a % 60) == 0 else (60 - (a % 60))
            if complement in hash:
                count += hash[complement]
            hash[a%60] += 1

        
        return count

        
        