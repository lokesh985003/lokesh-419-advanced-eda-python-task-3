class Solution(object):
    def maxProduct(self, nums):
        a = max(nums)
        nums.remove(a)
        b = max(nums)
        c = (a - 1) * (b - 1)
        return c

sol = Solution()
print(sol.maxProduct([3, 4, 5, 2]))   
print(sol.maxProduct([1, 5, 4, 5]))   
print(sol.maxProduct([3, 7]))    
