class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        prev = [1]
        res.append(prev)
        for i in range(2, numRows + 1):
            curr = [prev[0]]
            for j in range(1, len(prev)):
                curr.append(prev[j - 1] + prev[j])
            curr.append(prev[len(prev) - 1])
            res.append(curr)
            prev = curr
        return res
        
        