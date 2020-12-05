class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k ==0:
            return [0]*len(code)
        a=code+code
        
        if k>0:
            for i in range(len(code)):
                code[i]=sum(a[i+1:i+1+k])

        if k<0:
            for i in range(len(code)):
                code[i]=sum(a[len(code)+i+k:len(code)+i]) 

        return code
