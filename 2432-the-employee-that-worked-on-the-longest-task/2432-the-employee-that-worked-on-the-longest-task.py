class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        max_id = logs[0][0]
        max_dur = logs[0][1]
        last_end = logs[0][1]
        for i in range(1, len(logs)):
            if logs[i][1] - last_end > max_dur:
                max_id = logs[i][0]
                max_dur = logs[i][1] - last_end
            elif logs[i][1] - last_end == max_dur:
                max_id = min(max_id, logs[i][0])
            last_end = logs[i][1]
        return max_id
        