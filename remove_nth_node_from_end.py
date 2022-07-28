# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        def get_the_distance(head):
            if head.next == None:
                return 1
            count = 1 + get_the_distance(head.next)
            if count == n+1:
                head.next_node = head.next_node.next_node
            return count
        get_the_distance(head)
        return head
        