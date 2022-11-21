class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key = key.replace(' ','')
        lToALpha = {}
        start_pos = ord('a')
        for l in key:
            if l not in lToALpha.keys():
                s = chr(start_pos + len(lToALpha.keys()))
                lToALpha[l] = s
        res = []
        for l_m in message:
            if l_m != ' ':
                res.append(lToALpha.get(l_m))
            else:
                res.append(l_m)
        return ''.join(res)
        
        