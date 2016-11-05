from algore.structures import DoublyLinkedList
from unittest import TestCase

class TestDoublyLinkedList(TestCase):

    def setUp(self):
        self.dll = DoublyLinkedList()

    def test_dll_with_0_items(self):
        self.assertEqual(self.dll.root.value, None)
        self.assertIs(self.dll.iter, self.dll.root)
        self.assertEqual(self.dll.tail, None)
        with self.assertRaises(IndexError):
            self.dll[0]

    def test_dll_with_1_item(self):
        self.dll.insert(3)
        self.assertEqual(self.dll[0], 3)
        self.assertIs(self.dll.root, self.dll.tail)
        self.assertEqual(len(self.dll), 1)
        with self.assertRaises(IndexError):
            self.dll[1]

    def test_dll_with_2_item(self):
        self.dll.insert(3)
        self.dll.insert(4)
        self.assertEqual(self.dll[0], 3)
        self.assertEqual(self.dll[1], 4)
        self.assertEqual(self.dll.tail.value, 4)
        self.assertIs(self.dll.tail.next, self.dll.root)
        self.assertIs(self.dll.tail.prev, self.dll.root)
        self.assertEqual(len(self.dll), 2)
        with self.assertRaises(IndexError):
            self.dll[2]

    def test_dll_with_n_item(self):
        self.dll.insert(-1)
        self.dll.insert(0)
        for i in range(2, 100):
            self.dll.insert(i)
            self.assertEqual(self.dll[i], i)
            self.assertEqual(self.dll.root.prev.value, i)
            self.assertEqual(len(self.dll), i+1)
            with self.assertRaises(IndexError):
                self.dll[i+1]

    def test_dll_pop_out_of_range(self):
        self.dll.insert(1)
        with self.assertRaises(IndexError):
            self.dll.pop(1)

    def test_dll_pop_with_n_items(self):
        for i in range(100):
            self.dll.insert(i)
        self.assertEqual(self.dll.pop(), 0)
        self.assertEqual(self.dll.pop(27), 28)
        self.assertEqual(self.dll.pop(86), 88)
        self.assertEqual(self.dll.pop(96), 99)

    def test_dll_reverse_0_items(self):
        reversed_dll = self.dll.reverse()
        self.assertTrue(isinstance(reversed_dll, DoublyLinkedList))

    def test_dll_reverse_n_items(self):
        for i in range(100):
            self.dll.insert(i)
            reversed_dll = self.dll.reverse()
            expected = list(range(0, i+1))
            expected.reverse()
            self.assertEqual(str(reversed_dll), str(expected).replace(' ',''))
            self.assertTrue(isinstance(reversed_dll, DoublyLinkedList))
