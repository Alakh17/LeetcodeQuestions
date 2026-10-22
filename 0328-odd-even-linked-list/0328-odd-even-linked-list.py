# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head
        curr = head
        temp = head.next
        temp_c = temp

        while temp is not None and temp.next is not None:
            curr.next = curr.next.next
            curr = curr.next
            temp.next = temp.next.next
            temp = temp.next
        curr.next = temp_c
        return head
        