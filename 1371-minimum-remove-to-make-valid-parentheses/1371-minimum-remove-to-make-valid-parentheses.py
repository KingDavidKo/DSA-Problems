class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        output = ""
        remove = []
        for i in range(len(s)):
            if s[i] == ")" and len(stack) == 0:
                remove.append(i)
                output += ")"
            elif s[i] == "(":
                stack.append(i)
                output += "("
            elif s[i] == ")":
                stack.pop()
                output += ")"
            else:
                output += s[i]
        count = 0
        arr = list(output)
        fix = stack[:] + remove[:]
        fix.sort()


        for i in fix:
            arr.pop(i - count)
            count += 1

        

        output = ''.join(arr)

        return output