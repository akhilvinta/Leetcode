
def isValid(s: str) -> bool:
    open, closed = {}, {}
    open["("], open["{"], open["["]  = 0, 0, 0
    closed[")"], closed["}"], closed["]"] = 0, 0, 0
    
    stack = []
    for i in range(len(s)):
        if s[i] in open:
            open[s[i]] += 1
            stack.insert(0,s[i])
        elif s[i] in closed:
            if not stack:
                return False
            closed[s[i]] += 1
            if s[i] == ')':
                if stack[0] != '(':
                    return False
            elif s[i] == '}':
                if stack[0] != '{':
                    return False
            elif s[i] == ']':
                if stack[0] != '[':
                    return False
            else:
                return False
            stack.pop(0)
                
    return open["("] == closed[")"] and open["{"] == closed["}"] and open["["] == closed["]"]







    
                
            