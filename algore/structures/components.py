class Node(object):
    def __init__(self, value=None, next=None, prev=None, circular=False):
        self.value = value
        self.next = self if circular else next
        self.prev = self if circular else prev
