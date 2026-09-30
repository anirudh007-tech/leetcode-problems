
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        current = 0
        temp = self.head

        while temp is not None and current <= index:
            if current == index:
                return temp.data
            else:
                temp = temp.next
                current += 1

        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        temp = self.head
        new_node = Node(val)

        while index > 1 and temp is not None:
            temp = temp.next
            index -= 1

        if temp is not None:
            new_node.next = temp.next
            temp.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return
        elif index == 0:
            self.head = self.head.next
            return

        temp = self.head

        while index > 1 and temp is not None:
            temp = temp.next
            index -= 1

        if temp is None or temp.next is None:
            return

        temp.next = temp.next.next