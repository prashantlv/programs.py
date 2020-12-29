import random
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = [i for i in A if i%2==0]
        odd = [j for j in A if j%2!=0]
        even.extend(odd)
        return even
            