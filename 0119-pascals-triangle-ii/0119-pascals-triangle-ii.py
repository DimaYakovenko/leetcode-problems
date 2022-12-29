class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1]
        if rowIndex == 0:
            return prev
        for i in range(1, rowIndex + 1):
            curr = [prev[0]]
            for j in range(1, len(prev)):
                curr.append(prev[j - 1] + prev[j])
            curr.append(prev[len(prev) - 1])
            prev = curr
        return curr