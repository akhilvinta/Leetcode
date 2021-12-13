# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return str(self.x) + "," + str(self.y)

class Solution:
    def mergeKLists(self, ret: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = []
        for i in range(len(ret)):
            if ret[i]:
                lists.append(ret[i])
        if not lists:
            return None
        
        nodeList = []
        retList = ListNode(0)
        tempNode = retList
        for i in range(len(lists)):
            nodeList.append(Point(i,lists[i].val))
        while 1:
            nodeList = sorted(nodeList, key=lambda x: x.y)
            tempNode.next = ListNode(nodeList[0].y)
            tempNode = tempNode.next
            lists[nodeList[0].x] = lists[nodeList[0].x].next
            if lists[nodeList[0].x] == None:
                nodeList.pop(0)
            else:
                nodeList[0].y = lists[nodeList[0].x].val
            if not nodeList:
                break
                
        retList = retList.next
        return retList
    