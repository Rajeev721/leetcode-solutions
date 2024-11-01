# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        prev = ListNode()
        prev.next = head
        slow = prev

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        temp = slow

        slow.next =  slow.next.next
        return prev.next