class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        mini = [min(x) for x in matrix]
        maxi = [max(i) for i in zip(*matrix)]
    
        if max(mini) == min(maxi):
            return [max(mini)]
            #return []