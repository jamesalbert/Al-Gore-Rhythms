from algore.structures import CircularDoublyLinkedList, LinkedList
from unittest import TestCase


class TestLinkedList(TestCase):

    def setUp(self):
        self.ll = LinkedList()

    def test_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            self.ll.insert(3)
        with self.assertRaises(NotImplementedError):
            self.ll.pop(3)
        with self.assertRaises(NotImplementedError):
            self.ll.reverse()


class TestDoublyLinkedList(TestCase):

    def setUp(self):
        self.cdll = CircularDoublyLinkedList()

    def test_cdll_with_0_items(self):
        self.assertEqual(self.cdll.root.value, None)
        self.assertIs(self.cdll.iter, self.cdll.root)
        self.assertEqual(self.cdll.tail, None)
        with self.assertRaises(IndexError):
            self.cdll[0]

    def test_cdll_with_1_item(self):
        self.cdll.insert(3)
        self.assertEqual(self.cdll[0], 3)
        self.assertIs(self.cdll.root, self.cdll.tail)
        self.assertEqual(len(self.cdll), 1)
        with self.assertRaises(IndexError):
            self.cdll[1]

    def test_cdll_with_2_item(self):
        self.cdll.insert(3)
        self.cdll.insert(4)
        self.assertEqual(self.cdll[0], 3)
        self.assertEqual(self.cdll[1], 4)
        self.assertEqual(self.cdll.tail.value, 4)
        self.assertIs(self.cdll.tail.next, self.cdll.root)
        self.assertIs(self.cdll.tail.prev, self.cdll.root)
        self.assertEqual(len(self.cdll), 2)
        with self.assertRaises(IndexError):
            self.cdll[2]

    def test_cdll_with_n_item(self):
        self.cdll.insert(-1)
        self.cdll.insert(0)
        for i in range(2, 100):
            self.cdll.insert(i)
            self.assertEqual(self.cdll[i], i)
            self.assertEqual(self.cdll.root.prev.value, i)
            self.assertEqual(len(self.cdll), i+1)
            with self.assertRaises(IndexError):
                self.cdll[i+1]

    def test_cdll_pop_out_of_range(self):
        self.cdll.insert(1)
        with self.assertRaises(IndexError):
            self.cdll.pop(1)

    def test_cdll_pop_with_n_items(self):
        for i in range(100):
            self.cdll.insert(i)
        self.assertEqual(self.cdll.pop(), 0)
        self.assertEqual(self.cdll.pop(27), 28)
        self.assertEqual(self.cdll.pop(86), 88)
        self.assertEqual(self.cdll.pop(96), 99)

    def test_cdll_reverse_0_items(self):
        reversed_cdll = self.cdll.reverse()
        self.assertTrue(isinstance(reversed_cdll, CircularDoublyLinkedList))

    def test_cdll_reverse_n_items(self):
        for i in range(100):
            self.cdll.insert(i)
            reversed_cdll = self.cdll.reverse()
            expected = list(range(0, i+1))
            expected.reverse()
            self.assertEqual(str(reversed_cdll),
                             str(expected).replace(' ', ''))
            self.assertTrue(
                isinstance(
                    reversed_cdll,
                    CircularDoublyLinkedList))
