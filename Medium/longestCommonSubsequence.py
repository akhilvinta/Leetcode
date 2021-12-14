


def longestCommonSubsequence(s1, s2, index1, index2):
    print(str(index1) + "," + str(index2))
    if index1 >= len(s1) or index2 >= len(s2):
        return 0
    matchedTotal = -1
    unmatchedTotal = -1
    if s1[index1] == s2[index2]:
        matchedTotal = 1 + longestCommonSubsequence( s1, s2, index1+1, index2+1 )
    else:
        unmatchedTotal = max( longestCommonSubsequence( s1, s2, index1+1, index2 ), longestCommonSubsequence( s1, s2, index1, index2+1 ) )
    
    return max(unmatchedTotal, matchedTotal)

s1 = "abcde"
s2 = "ace"

x = longestCommonSubsequence(s1, s2, 0, 0)
print(x)
