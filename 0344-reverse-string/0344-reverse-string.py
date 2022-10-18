class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        min_right_bound = len(s)
        for i in range(len(s)):
            if i >= min_right_bound:
                break
            min_right_bound = len(s) - 1 - i
            s[i], s[min_right_bound] = s[min_right_bound], s[i]
            