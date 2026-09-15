class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)

        while head:
            node = head
            head = head.next

            prev = dummy
            while prev.next and prev.next.val < node.val:
                prev = prev.next

            node.next = prev.next
            prev.next = node

        return dummy.next
        