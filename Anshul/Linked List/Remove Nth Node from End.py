class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        return

linkedList = ListNode(0)
linkedList.next = ListNode(1)
linkedList.next.next = ListNode(2)
linkedList.next.next.next = ListNode(3)
linkedList.next.next.next.next = ListNode(4)
linkedList.next.next.next.next = ListNode(5)
linkedList.next.next.next.next.next = ListNode(6)
linkedList.next.next.next.next.next.next = ListNode(7)
linkedList.next.next.next.next.next.next.next = ListNode(8)
linkedList.next.next.next.next.next.next.next.next = ListNode(9)
linkedList.next.next.next.next.next.next.next.next.next = None


def find(head, n):
    counter = 1
    f = head
    s = head
    while counter <= n:
        s = s.next
        counter += 1
    if s is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    while s.next is not None:
        s = s.next
        f = f.next
    f.next = f.next.next
