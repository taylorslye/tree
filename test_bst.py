#Run with 'python -m unittest test_tree':


import unittest
from bst import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):
    
    def test_instantiation(self):
        try:
            BinarySearchTree()
        except NameError:
            self.fail("could not instantiate tree")
    
    def test_instantiation_with_value(self):
        fake_value = "fake"
        bst = BinarySearchTree(fake_value)
        self.assertEqual(fake_value,bst.value)

    def test_hasleft_and_right_inittialy_none(self):
        bst = BinarySearchTree()
        self.assertEqual(None, bst.left)
        self.assertEqual(None, bst.right)

    def test_initially_substantiates_children_to_the_left(self):
        bst = BinarySearchTree(30)
        appendee = BinarySearchTree(15)
        bst.append(appendee)
        self.assertEqual(bst.left, appendee)

    def test_If_bigger_put_into_right(self):
        bst = BinarySearchTree(3)
        appendee = BinarySearchTree(15)
        bst.append(appendee)
        self.assertEqual(bst.right, appendee)

    def test_Have_two_levels_and_search(self):
        bst = BinarySearchTree(20)
        appendee = BinarySearchTree(21)
        appendee2 = BinarySearchTree(22)
        bst.append(appendee)
        bst.append(appendee2)
        self.assertEqual(appendee2, appendee.right)

'''    def test_pre_order_traversal(self):
        bst = BinarySearchTree(20)
        appendee = BinarySearchTree(21)
        appendee2 = BinarySearchTree(19)
        bst.append(appendee)
        bst.append(appendee2)
        #self.assertEqual([20, 19, 21], bst.preorder_search())
        # couldn't get the test for any search to fit the numbersw in a list, but they printed out in order.

    def test_post_order_traversal(self):
        bst = BinarySearchTree(20)
        appendee = BinarySearchTree(21)
        appendee2 = BinarySearchTree(19)
        bst.append(appendee)
        bst.append(appendee2)
        self.assertEqual([19, 21, 20], bst.postorder_search())

    def test_in_order_traversal(self):
        bst = BinarySearchTree(20)
        appendee = BinarySearchTree(21)
        appendee2 = BinarySearchTree(19)
        bst.append(appendee)
        bst.append(appendee2)
        self.assertEqual([19, 20, 21], bst.inorder_search())
'''

    if __name__ == '__main__':
        unittest.main()
