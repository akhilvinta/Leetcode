import sys



dict = {}

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        ret = self.helper(jobDifficulty, d)
        # print(2**31-1)
        return -1 if ret >= 10000 else ret
        
        
    def helper(self, jobDifficulty, d):
        
        if (str(jobDifficulty) + "," + str(d)) in dict:
            return dict[str(jobDifficulty) + "," + str(d)]
        
        if len(jobDifficulty) < d:
            return 10000
        if d == 1:
            return max(jobDifficulty)
        
        min = 10000
        for i in range(len(jobDifficulty)):
            upToSplit = jobDifficulty[0:i+1]
            splitToFinish = jobDifficulty[i+1:]
            diffOfPath = max(upToSplit) + self.helper(splitToFinish, d-1)
            if diffOfPath < min:
                min = diffOfPath
    
        dict[str(jobDifficulty) + "," + str(d)] = min
        return min

        
        
        
        