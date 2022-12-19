class Solution:
    def checkRecord(self, s: str) -> bool:
        abs_count = 0
        late_count = 0
        for i in s:
            if i == 'A':
                abs_count += 1
            if i == 'L':
                late_count += 1
            else: 
                late_count = 0
            if abs_count > 1 or late_count == 3:
                return False
        return True