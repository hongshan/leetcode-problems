# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        current = head
        def nextval(l):
            return l.next.val if (l and l.next) else 0
        def nextnode(l):
            return l.next if l else None
        v1 = l1.val
        v2 = l2.val
        leading = 0
        while l1 or l2:
            sumval = v1 + v2 + leading
            leading = sumval / 10
            sumval = sumval % 10
            temp = ListNode(sumval)
            current.next = temp
            current = current.next
            v1 = nextval(l1)
            v2 = nextval(l2)
            l1 = nextnode(l1)
            l2 = nextnode(l2)
        if leading:
            temp = ListNode(leading)
            current.next = temp

        return head.next
        