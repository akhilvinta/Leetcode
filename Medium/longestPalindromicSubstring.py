
def longestPalindrome(s: str) -> str:
    dp  = ['a'] * len(s)
    for i in range(len(dp)):
        dp[i] = ['a'] * len(s)
    for i in range(len(dp)):
        dp[i][i] = 1
        if (i+1) < len(dp):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
            else:
                dp[i][i+1] = 0
    
    interval = 2
    while interval < len(dp):
        for start in range(len(dp)):
            end = start + interval
            if end < len(dp):
                if dp[start+1][end-1] == 1 and (s[start] == s[end]):
                    dp[start][end] = 1
                else:
                    dp[start][end] = 0
        interval += 1
    
    
    maxLength = -1
    start = -1
    end = -1
    for i in range(len(dp)):
        for j in range(i,len(dp)):
            if (j - i + 1) > maxLength and dp[i][j] == 1:
                maxLength = (j - i + 1)
                start = i
                end = j
    ret = s[start:end+1]
    return ret
                    

print(longestPalindrome("ansdsnw"))


            
            
        