from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    if list1 is None:
        return list2

    if list1.val <= list2.val:
        current_node: ListNode = list1
        support_node: ListNode = list2
    else:
        current_node: ListNode = list2
        support_node: ListNode = list1

    start_node: ListNode = current_node

    while current_node.next and support_node:
        if current_node.val <= support_node.val < current_node.next.val:
            next_next_node = current_node.next
            current_node.next = ListNode(support_node.val, next_next_node)
            if not support_node.next:
                return start_node
            support_node = support_node.next
        current_node = current_node.next

    current_node.next = support_node

    return start_node


list_1 = ListNode(1, ListNode(2, ListNode(4)))
list_2 = ListNode(1, ListNode(3, ListNode(4)))

lst = merge_two_lists(list_1, list_2)

while lst:
    print(lst.val)
    lst = lst.next
