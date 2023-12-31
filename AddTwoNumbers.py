# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def construct(l):
            sum = 0
            i = 0
            node = l
            while True:
                sum = sum + node.val * pow(10, i)
                if node.next == None:
                    break
                node = node.next
                i = i + 1
            return sum

        def destruct(num):
            first_node = ListNode(val=0, next=None)
            prev_node = first_node
            i = 0
            while True:
                value = int(
                    round(num % pow(10, i + 1), pow(10, i)) / pow(10, i)
                )
                prev_node.val = value
                print(value)
                i = i + 1
                if num / pow(10, i) < 1:
                    break
                node = ListNode(val=0, next=None)
                prev_node.next = node
                prev_node = node

            return first_node

        x = construct(l1)
        y = construct(l2)
        l3 = destruct(x + y)
        return l3
