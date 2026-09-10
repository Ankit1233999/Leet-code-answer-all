class Solution:
    def sortedListToBST(self, head):
        if head is None:
            return None

        
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        

        
        if prev:
            prev.next = None

        
        root = TreeNode(slow.val)

        
        if slow == head:
            return root

        
        root.left = self.sortedListToBST(head)

        
        root.right = self.sortedListToBST(slow.next)

        return root
        