class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if not stack:
                    return False
                
                top_char = stack.pop()
                
                if char == ')' and top_char != '(': return False
                if char == ']' and top_char != '[': return False
                if char == '}' and top_char != '{': return False
                
        return len(stack) == 0