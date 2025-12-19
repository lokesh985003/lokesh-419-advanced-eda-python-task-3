class Solution(object):
    def numberOfSteps(self, num):
        a = 0
        while num > 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num = num - 1
            a += 1
        return a
sol = Solution()
print(sol.numberOfSteps(14))   
print(sol.numberOfSteps(8))   
print(sol.numberOfSteps(123))  
