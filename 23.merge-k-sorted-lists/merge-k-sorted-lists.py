# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:  # Check for input:[]
            return ListNode().next

        heap = []
        for i in range(len(lists)):
            if not lists[i]:
                continue
            heap.append(tuple((lists[i].val, i, lists[i])))

        if not heap:  # Check for input:[[]]
            return ListNode().next

        heapq.heapify(heap)

        head = tail = None
        while heap:
            i, node = heapq.heappop(heap)[1:]
            if head is None:  # First element
                head = tail = node
            else:
                tail.next = node
                tail = node

            if node.next:
                heapq.heappush(heap, (tail.next.val, i, tail.next))

        return head