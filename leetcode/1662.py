class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        ln1 = len(word1)
        ln2 = len(word2)
        wd1,wd2 = '',''
        for i in range(ln1):
            wd1 += word1[i]
        for j in range(ln2):    
            wd2 += word2[j]
        return wd1 == wd2