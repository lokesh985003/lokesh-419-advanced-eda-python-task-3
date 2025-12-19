class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        a = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                a += 1
        return a
sol = Solution()
print(sol.busyStudent([1, 2, 3], [3, 2, 7], 4))  
print(sol.busyStudent([4], [4], 4))             
