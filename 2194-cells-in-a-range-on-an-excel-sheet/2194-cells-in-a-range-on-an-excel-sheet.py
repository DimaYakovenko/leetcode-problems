class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        cells_list = s.split(':')
        c_from = ord(cells_list[0][0])
        r_from = int(cells_list[0][1])
        c_to = ord(cells_list[1][0])
        r_to = int(cells_list[1][1])

        res = []
        while c_from <= c_to:
            row = r_from
            while row <= r_to:
                res.append(chr(c_from) + str(row))
                row += 1
            c_from += 1

        res.sort()
        return res
        