class Solution:
    @staticmethod
    @cache
    def get_reverse(s):
        if len(s) <= 1:
            return s
        else:
            return Solution.get_reverse(s[1:]) + s[0]
        
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for v in range(num + 1):
            if v + int(Solution.get_reverse(str(v))) == num:
                return True
        return False
        