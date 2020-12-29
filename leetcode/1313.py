# class Solution:
#     def decompressRLElist(self, nums: List[int]) -> List[int]:
#         l = len(nums)
#         li = []
#         for i in range(0,l,2):
#             for j in range(0,l,2):
#                 n = nums[i]
#                 for k in range(n):
#                     li.append(nums[j])
#         return li


# class Solution:
#     def decompressRLElist(self, nums: List[int]) -> List[int]:
#         arr = []
#         for i in range(0, int(len(nums)/2)):
#             for k in range(0, nums[2*i]):
#                 arr.append(nums[2*i+1])
#         return arr

# Input: nums = [1,2,3,4]
# Output: [2,4,4,4]

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        li = []
        for i in range(0,len(nums),2):
            pair1 = nums[i]
            pair2 = nums[i+1]
            temp = pair1 * [pair2]
            li.extend(temp)
        return li            