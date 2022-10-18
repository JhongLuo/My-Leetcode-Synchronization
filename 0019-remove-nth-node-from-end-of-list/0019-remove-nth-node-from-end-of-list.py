# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        node = head
        while node:
            node = node.next
            length += 1
        n = length - n
        handle = ListNode(next=head)
        node = handle
        idx = 0
        while node.next:
            if idx == n:
                node.next = node.next.next
                break
            idx += 1
            node = node.next
        return handle.next