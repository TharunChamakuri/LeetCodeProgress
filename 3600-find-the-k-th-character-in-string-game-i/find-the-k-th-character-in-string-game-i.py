class Solution(object):
    def kthCharacter(self, k):
        length = 1
        shifts = 0
        while length < k:
            length *= 2
            shifts += 1
        total_shifts = 0
        while shifts > 0:
            length //= 2
            if k > length:
                k -= length
                total_shifts += 1
            shifts -= 1
        ch = ord('a') + total_shifts % 26
        return chr(ch)
        