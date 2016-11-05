
class Node(object):
    def __init__(self, value=None, next=None, prev=None, root=None):
        self.value = value
        self.next = self if root else next
        self.prev = self if root else prev

class DoublyLinkedList(object):
    def __init__(self):
        self.root = Node(root=True)
        self.iter = self.root
        self.tail = None
        self.len = 0

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
        node = None
        if index < len(self) / 2:
            node = self.root
            attr = 'next'
        else:
            node = self.tail
            attr = 'prev'
            index += 1
        for i in range(index):
            node = getattr(node, attr)
        if node is self.root:
            self.root = node.next
        elif node is self.tail:
            self.tail = node.prev
        node.next.prev = node.prev
        node.prev.next = node.next
        self.len -= 1
        return node

    def reverse(self):
        ll = DoublyLinkedList()
        node = self.tail
        while True:
            ll.insert(node.value)
            node = node.prev
            if len(ll) == len(self):
                break
        return ll

    def printf(self, node):
        if node.value == self.tail.value:
            return node.value
        return ','.join([node.value, self.printf(node.next)])

    def __str__(self):
        return self.printf(self.root)

    def __len__(self):
        return self.len

    def __getitem__(self, index):
        if index >= len(self):
            raise Exception('index {0} out of range'.format(index))
        for i in range(index):
            self.iter = self.iter.next
        item = self.iter.value
        self.iter = self.root
        return item
