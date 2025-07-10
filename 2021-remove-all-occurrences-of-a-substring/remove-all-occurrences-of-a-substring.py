class Solution(object):
    def removeOccurrences(self, s, part):
        def check(stack , part):
            for i in range(len(part)):
                if stack[i] != part[i]:
                    return False
            return True
        stack = []
        for ch in s:
            stack.append(ch)
            if len(stack) >= len(part) and stack[-1] == part[len(part)-1]:
                ind = len(stack) - len(part)
                if check(stack[ind:] , part):
                    for i in range(len(part)):
                        stack.pop()
        return "".join(stack)
