# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        temp = l3

        while 1:
            if l1 != None and l2 != None:
                if l1.val <= l2.val:
                    temp.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    temp.next = ListNode(l2.val)
                    l2 = l2.next
            elif l1 != None and l2 == None:
                temp.next = ListNode(l1.val)
                l1 = l1.next
            elif l1 == None and l2 != None:
                temp.next = ListNode(l2.val)
                l2 = l2.next
            elif l1 == None and l2 == None:
                break
            temp = temp.next

        l3 = l3.next
        return l3