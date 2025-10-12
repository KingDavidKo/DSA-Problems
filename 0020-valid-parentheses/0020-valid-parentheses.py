class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i == "(":
                stack.append(")")
            elif i == "[":
                stack.append("]")
            elif i == "{":
                stack.append("}")
            else:
                if stack:
                    if i == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if (stack):
            return False
        return True

        