class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
        self.counter_nums2 = Counter(nums2)

    def add(self, index, val):
        prev_val = self.nums2[index]
        self.counter_nums2[prev_val] -= 1

        if self.counter_nums2[prev_val] == 0:
            del self.counter_nums2[prev_val]

        self.nums2[index] += val
        new_val = self.nums2[index]
        self.counter_nums2[new_val] += 1
    def count(self, tot):
        count = 0
        for num in self.nums1:
            complement = tot - num
            count += self.counter_nums2.get(complement , 0)
        return count
