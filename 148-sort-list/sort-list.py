# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        nums=[]
        curr = ans = head
        while ans:
            nums.append(ans.val)
            ans=ans.next
        nums.sort()
        count = 0
        while curr:
            curr.val = nums[count]
            count = count +1
            curr=curr.next
        return head