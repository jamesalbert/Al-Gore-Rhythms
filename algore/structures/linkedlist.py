from .components import Node


class LinkedList(object):
    def __init__(self):
        self.root = Node()
        self.iter = self.root
        self.tail = None
        self.len = 0

    def insert(self, item):
        raise NotImplementedError

    def pop(self, index=0):
        raise NotImplementedError

    def reverse(self):
        raise NotImplementedError

    def printf(self, node):
        if node is self.tail:
            return str(node.value)
        return ','.join([str(node.value), self.printf(node.next)])

    def __str__(self):
        return '[{0}]'.format(self.printf(self.root))

    def __len__(self):
        return self.len

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError('index {0} out of range'.format(index))
        for i in range(index):
            self.iter = self.iter.next
        item = self.iter.value
        self.iter = self.root
        return item


class CircularDoublyLinkedList(LinkedList):
    def __init__(self):
        super().__init__()
        self.root = Node(circular=True)
        self.iter = self.root

    def insert(self, item):
        if not self.tail:
            '''0 nodes in list'''
            self.root.value = item
            self.tail = self.root
        elif self.root is self.tail:
            '''1 node in list'''
            self.tail = Node(item, self.root, self.root)
            self.root.next = self.tail
            self.root.prev = self.tail
        else:
            '''2 or more nodes in list'''
            self.root.prev = Node(item, self.root, self.tail)
            self.tail.next = self.root.prev
            self.tail = self.tail.next
        self.len += 1
        return self

    def pop(self, index=0):
        if index + 1 > len(self):
            raise IndexError('index {0} out of range'.format(index))
        node = None
        node = self.root
        attr = 'next'
        for i in range(index):
            node = getattr(node, attr)
        if node is self.root:
            self.root = node.next
        elif node is self.tail:
            self.tail = node.prev
        node.next.prev = node.prev
        node.prev.next = node.next
        self.len -= 1
        return node.value

    def reverse(self):
        ll = CircularDoublyLinkedList()
        if len(self) is 0:
            return ll
        node = self.tail
        while True:
            ll.insert(node.value)
            node = node.prev
            if len(ll) == len(self):
                break
        return ll
