class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        number = [int(c) for c in str(n)]
        number = [0] + number
        total = sum(number)

        def find_last_non_zero(number):
            for i in range(len(number) - 1, -1, -1):
                if number[i] != 0:
                    return i            
        pos = find_last_non_zero(number)
        
        while total > target:
            number[pos] = 0
            pos -= 1
            while number[pos] == 9:
                number[pos] = 0
                pos -= 1
            number[pos] += 1
            total = sum(number)

        # print(total, number)
        
        return int(''.join([str(v) for v in number])) - n
