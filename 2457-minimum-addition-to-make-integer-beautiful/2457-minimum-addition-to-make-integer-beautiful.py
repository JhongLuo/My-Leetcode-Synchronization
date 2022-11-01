class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        number = [int(c) for c in str(n)]
        number = [0] + number
        total = sum(number)

        def find_last_non_zero(number):
            for i in range(len(number) - 1, -1, -1):
                if number[i] != 0:
                    return i            

        while total > target:
            pos = find_last_non_zero(number)
            number[pos] = 0
            for i in range(pos - 1, -1, -1):
                if number[i] != 9:
                    number[i] += 1
                    break
                else:
                    number[i] = 0
            total = sum(number)

        # print(total, number)
        
        return int(''.join([str(v) for v in number])) - n
