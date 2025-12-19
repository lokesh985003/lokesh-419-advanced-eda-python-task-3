class Solution(object):
    def countBits(self, n):
        a = []
        for i in range(n + 1):
            count = 0
            x = i
            while x > 0:
                if x % 2 == 1:
                    count += 1
                x = x // 2
            a.append(count)
        return a

sol = Solution()
print(sol.countBits(2))  
print(sol.countBits(5))  
