class BinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None) -> None:
            self.data = data
            self.left = left
            self.right = right

    def preorder(self, node):

        if node == None : return

        self.preorder(node.left)
        print(node.data)
        self.preorder(node.right)

binaryTree = BinaryTree()
root = BinaryTree.Node(1, 
                       BinaryTree.Node(2, 
                                       BinaryTree.Node(4, 
                                                       BinaryTree.Node(8), 
                                                       BinaryTree.Node(9)
                                                      ), 
                                       BinaryTree.Node(5, 
                                                       BinaryTree.Node(10), 
                                                       BinaryTree.Node(11)
                                                      )
                                      ), 
                       BinaryTree.Node(3, 
                                       BinaryTree.Node(6, 
                                                       BinaryTree.Node(12), 
                                                       BinaryTree.Node(13)
                                                      ), 
                                       BinaryTree.Node(7, 
                                                       BinaryTree.Node(14), 
                                                       BinaryTree.Node(15)
                                                      )
                                      )
                      )

binaryTree.preorder(root)