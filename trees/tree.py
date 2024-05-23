"""A tree stores elements in a hierachically. Each element is called a node, each 
node has a unique parent and zero or more children. The root element has no parent.
"""
from abc import abstractmethod, ABC


class Tree(ABC):
    
    class Node(ABC):
        
        @abstractmethod
        def node(self):
            pass
        
        @abstractmethod
        def __eq__(self, other):
            pass
        
        @abstractmethod
        def __ne__(self, other):
            return not (self == other)

    # ---- Abstract methods the concret class of Tree must implement. ---- #
    @abstractmethod
    def __len__(self):
        pass
    
    @abstractmethod
    def root(self):
        pass
    
    @abstractmethod
    def parent(self, node):
        pass
    
    @abstractmethod
    def children(self, node):
        pass
    
    @abstractmethod
    def num_children(self, node):
        pass
    
    # ---- Concrete implementations provided. ---- #
    def is_root(self, node):
        return self.root() == node
        
    def is_leaf(self, node):
        return self.num_children(node) == 0
        
    def is_empty(self):
        return len(self) == 0

    def depth(self, node):
        """Return how deep given node is from root node."""
        if self.is_root(node):
            return 0
        return 1 + self.depth(self.parent(node))
        
    def height(self, node=None):
        """Returns maximum depth of all leaves from given node as root."""
        if node is None:
            node = self.root()
        
        return self._height(node)
        
    def _height(self, node):
        if self.is_leaf(node):
            return 0
        return 1 + max(self._height(n) for n in self.children(node))
