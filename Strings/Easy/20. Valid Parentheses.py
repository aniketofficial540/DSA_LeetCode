class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for i in s:

            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                    
                top = len(stack)-1
                
                if i == ")" and stack[top] == "(":
                    stack.pop()
                elif i == "]" and stack[top] == "[":
                    stack.pop()
                elif i == "}" and stack[top] == "{":
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
