class Solution(object):
    def numTeams(self, rating):
        total = 0
        n = len(rating)
        for b in range(n):
            left_small = 0
            left_large = 0
            right_small = 0
            right_large = 0
            for a in range(b):
                if rating[a] < rating[b]:
                    left_small += 1
                elif rating[a] > rating[b]:
                    left_large += 1
            for c in range(b + 1, n):
                if rating[c] > rating[b]:
                    right_large += 1
                elif rating[c] < rating[b]:
                    right_small += 1
            total += left_small * right_large + left_large * right_small
        return total
sol = Solution()
print(sol.numTeams([2, 5, 3, 4, 1]))   
print(sol.numTeams([2, 1, 3]))         
print(sol.numTeams([1, 2, 3, 4]))      
print(sol.numTeams)
