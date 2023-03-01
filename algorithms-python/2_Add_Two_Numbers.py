'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Input: l1 = [0], l2 = [0]
Output: [0]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        fn = ""
        sn = ""
        while l1 is not None:
            fn += str(l1.val)
            l1 = l1.next
        
        while l2 is not None:
            sn += str(l2.val)
            l2 = l2.next

        tn = str(int(fn[::-1])+int(sn[::-1]))
        tn = list(map(int,tn))
        l3 = ListNode(val=tn[0], next=None)
        for i in range(1, len(tn)):
            l3 = ListNode(val=tn[i], next=l3)

        return l3