# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr1 = l1
        curr2 = l2
        send_list = []

        def append_to_list(send_list, val1, val2):
            while val1 is not None:
                send_list.append(val1.val)
                val1 = val1.next
            while val2 is not None:
                send_list.append(val2.val)
                val2 = val2.next
        append_to_list(send_list, curr1, curr2)
        send_list.sort()
        if send_list == []:
            return
        else:
            l3 = ListNode(send_list[0])
        curr = l3
        for i in range(len(send_list)):
            if i != 0:
                curr.next = ListNode(send_list[i])
                curr = curr.next
        return l3
