class Solution:
    def countTime(self, time: str) -> int:
        res = 1
        if time[0] == '?' and time[1] == '?':
            res *= 24
        elif time[0] == '?':
            res *= 3 if ord(time[1]) <= ord('3') else 2
        elif time[1] == '?':
            res *= 4 if ord(time[0]) == ord('2') else 10
        
        if time[3] == '?':
            res *= 6
        if time[4] == '?':
            res *= 10
        return res
            
        
        