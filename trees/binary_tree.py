from tree import Tree


class BinaryTree(Tree):
    
    class _Node(Tree.Node):
        pass
    
    
    def __len__(self):
        pass
    
    def children(self, node):
        pass
    
    def num_children(self, node):
        pass
    
    def parent(self, node):
        pass
    
    def root(self, node):
        pass


if __name__ == "__main__":
    bt = BinaryTree()