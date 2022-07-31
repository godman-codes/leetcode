# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, cur = dummy, head

        while cur and cur.next:
            sand = cur.next
            man = cur.next.next

            sand.next=cur
            cur.next = man

            prev.next = sand
            prev = cur
            cur = man
        return dummy.next
            

            