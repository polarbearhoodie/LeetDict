class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeLinked(list1, list2):
    merge = []
    if not list1 and not list2:
        if list1.data > list2.data:
            merge = list2
        else:
            merge = list1

    head = merge

    while list1 is not None or list2 is not None:
        if list1 is None or list1.data > list2.data:
            merge.next = list2
            merge = merge.next
            list2 = list2.next

        if list2 is None or list2.data > list1.data:
            merge.next = list1
            merge = merge.next
            list1 = list1.next

    return head


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    cur = dummy = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1, cur = list1.next, list1
        else:
            cur.next = list2
            list2, cur = list2.next, list2

    if list1 or list2:
        cur.next = list1 if list1 else list2

    return dummy.next

