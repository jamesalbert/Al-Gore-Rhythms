from algore.structures import Heap
from unittest import TestCase


class TestHeap(TestCase):

    def setUp(self):
        self.h = Heap()

    def test_insert_n_items(self):
        for i in range(100):
            self.h.insert(i)
            self.assertEqual(self.h.get_sorted(), list(range(0, i+1)))

    def test_delete_n_items(self):
        for i in range(100):
            self.h.insert(i)
        for i in range(99, -1, -1):
            self.h.delete(i)
            self.assertEqual(self.h.get_sorted(), list(range(0, i)))
