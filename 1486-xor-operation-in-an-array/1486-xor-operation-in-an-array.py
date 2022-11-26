class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = start
        # arr = [start]
        for i in range(1, n):
            # next_ = start + i * 2
            # arr.append(next_)
            res ^= start + i * 2
            # print('res ^ next = {} ^ {} = ',res + ' ^ ' + next_ + ' = ' + res)
        # print(arr)
        return res
        