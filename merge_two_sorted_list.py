# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        while list1.next != None and list2.next != None:
            if list1 >= list2.val:
                dummy.next = list1.val
                list1.val = list1.next
            else:
                dummy.next = list2.val
                list2.val = list2.next
            dummy.val = dummy.next

        while list1.next:
            dummy.next = list1.val
        while list2.next:
            dummy.next = list2.val
            dummy.val = dummy.next
        return dummy.next
