class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        history = []
        length = 1
        shifts = 0
        for op in operations:
            if length >= k:
                break
            history.append([length , op])
            length *= 2

        for i in range(len(history) - 1, -1, -1):
            prev_len , op = history[i]
            if k > prev_len:
                k -= prev_len
                if op == 1:
                    shifts += 1
        ch = ord("a") + shifts % 26
        return chr(ch)
        