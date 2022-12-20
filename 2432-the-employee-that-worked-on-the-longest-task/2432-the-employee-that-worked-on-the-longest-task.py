class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        start_prev = 0
        emp_id_to_dur = dict()
        for log in logs:
            emp_id = log[0]
            end_time = log[1]
            duration = end_time - start_prev
            start_prev = end_time
            
            if emp_id not in emp_id_to_dur or duration > emp_id_to_dur[emp_id]:
                emp_id_to_dur[emp_id] = duration
        emp_id_to_dur = sorted(emp_id_to_dur.items(), key=lambda i: (-i[1], i[0]) )
        return emp_id_to_dur[0][0]
        