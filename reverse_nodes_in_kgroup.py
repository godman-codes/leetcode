# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k: int):
        dummy = ListNode()
        cur = dummy
        def getKElement(head, k):
            small = ListNode()
            smart = small
            if not head:
                return None, None, None
            while k:
                if head:
                    smart.next = head
                    smart = smart.next
                    head = head.next
                    k -= 1
                else:
                    return small.next, None, 2
            smart.next = None
            return small.next, head, 3
        def reverseLinkedList(head):
            new_head = None
            matt = head
            curr = head
            previous = None
            if not head:
                return None, None
            while True:
                tmp = curr.next
                curr.next = previous
                previous = curr
                if not tmp:
                    break
                curr = tmp
            return curr, matt
        while True:
            if not head:
                return dummy
            trimmed_head, new_head, count = getKElement(head, k)
            if not trimmed_head and not new_head:
                return dummy.next
            elif new_head == None and count == 2:
                cur.next = trimmed_head
                return dummy.next
            else:
                reversed_g, last_element = reverseLinkedList(trimmed_head)
                cur.next = reversed_g
                cur = last_element
            head = new_head


# neetcode Solution
class Solution:
    def reverseKGroup(self, head, k: int):
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKthGroup(groupPrev, k)
            if not kth:
                break

            nextGroup = kth.next
            # reverse the group
            prev, cur = kth.next, groupPrev.next
            while cur != nextGroup:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next
        
    def getKthGroup(head, k):
        while head and k > 0:
            head = head.next
            k -= 1
        return head