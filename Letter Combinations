dict = {}
dict['2'] = ['a','b','c']
dict['3'] = ['d','e','f']
dict['4'] = ['g','h','i']
dict['5'] = ['j','k','l']
dict['6'] = ['m','n','o']
dict['7'] = ['p','q','r','s']
dict['8'] = ['t','u','v']
dict['9'] = ['w','x','y','z']


    
def letterCombinations(digits: str) -> List[str]:
    if not digits:
        return []
    return helper(digits, "", [])


def helper(digits, curString, retArr):
    if len(digits) == 0:
        retArr.append(curString)
    else:
        curDigit = digits[0]
        tempDigits = digits[1:]
        for letter in dict[curDigit]:
            helper(tempDigits, curString + letter, retArr)
    
    return retArr

        
        
        