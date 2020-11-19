class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        l = len(startTime)
        count = 0
        for i in range(l):
            if queryTime in range(startTime[i], endTime[i]+1):
                count += 1
        return count        