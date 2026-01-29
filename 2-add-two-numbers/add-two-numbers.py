# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            sum = carry
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            carry = sum // 10
            digit = sum % 10

            curr.next= ListNode(digit)
            curr = curr.next
        return dummy.next
        # t1 = None
        # t2 = dummy.next
        # t3 = t2.next

        # while not t3:
        #     t2.next = t1
        #     t1 = t2
        #     t2 = t3
        #     t3 = t3.next
        # dummy = t2
        # result = ""
        # while dummy:
        #     result= result + str(dummy.val)
        # return int(result)     

                

        