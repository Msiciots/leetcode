# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        
        dump = ListNode()
        dump.next = head
        
        total_node = 0
        tmp_ptr = dump
        while tmp_ptr.next:
            tmp_ptr = tmp_ptr.next
            total_node += 1
        
        tmp_ptr = dump
        for i in range(total_node - n):
            tmp_ptr = tmp_ptr.next
       
        if tmp_ptr.next == head:
            head = head.next
        else:
            tmp_ptr.next = tmp_ptr.next.next

        return head


