

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    l3 = ListNode(0)
    temp = l3
    carry = 0
    while 1:
        if l1 != None and l2 != None: 
            sum = l1.val + l2.val + carry
        elif l1 == None and l2 != None:
            sum = l2.val + carry
        elif l2 == None and l1 != None:
            sum = l1.val + carry
        else:
            break
        if sum > 9:
            sum = sum % 10        
            carry = 1
        else:
            carry = 0
        temp.next = ListNode(sum)
        temp = temp.next
        if l1 != None:
            l1 = l1.next
        if l2 != None:
            l2 = l2.next
    
    if carry == 1:
        temp.next = ListNode(1)
        
    
    l3 = l3.next
    return l3