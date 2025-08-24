from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    res = head
    while head and head.next:
        if head.val == head.next.val:
            head.next = head.next.next
        else:
            head = head.next

    return res


node = delete_duplicates(ListNode(1, ListNode(2, ListNode(2, ListNode(3, None)))))
