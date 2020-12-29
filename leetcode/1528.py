class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        z = dict(zip(indices,s))
        s,ln = '',len(indices)
        for i in range(ln):
            s += z[i]
        return s