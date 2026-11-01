class Solution:
    def addTwoNumbers(self, l1, l2):
        num1 = 0
        num2 = 0
        multiplier = 1

        while l1:
            num1 += l1.val * multiplier
            multiplier *= 10
            l1 = l1.next

        multiplier = 1

        while l2:
            num2 += l2.val * multiplier
            multiplier *= 10
            l2 = l2.next

        total = num1 + num2

        dummy = ListNode(0)
        current = dummy

        if total == 0:
            return dummy

        while total > 0:
            digit = total % 10
            current.next = ListNode(digit)
            current = current.next
            total //= 10

        return dummy.next