class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        prev = [1]
        res = []
        res.append(prev)
        for i in range(2, numRows + 1):
            curr = [prev[0]]
            for j in range(1, len(prev)):
                curr.append(prev[j -1 ] + prev[j])
                j +=1
            curr.append(prev[len(prev)-1])
            res.append(curr)
            prev = curr
        return res
    
        
        