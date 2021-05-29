url: https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        a =[]
        for i in range(1,len(intervals)):
            if len(intervals) == 1:
                a = intervals[0]
            elif intervals[i][0] <= intervals[i-1][1]:
                a.append([intervals[i-1][0], intervals[i][1]])
            else:
                a.append(intervals[i])
        return a        
        
