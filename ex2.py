import random
import matplotlib.pyplot as plt
import time
import sys

# Increase recursion limit to handle 1000 sequential insertions
sys.setrecursionlimit(3000)

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.balance = 0

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        """Insert a new key into the BST - iterative version"""
        new_node = TreeNode(key)
        
        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        while True:
            if key <= current.key:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right
        
        pivot = self.find_pivot(new_node)
        
        if pivot is None:
            print("Case #1: Pivot not detected")
        elif pivot.balance > 0:
            if new_node.key <= pivot.key:
                print("Case #2: A pivot exists, and a node was added to the shorter subtree")
            else:
                print("Case 3 not supported")
        else:
            if new_node.key > pivot.key:
                print("Case #2: A pivot exists, and a node was added to the shorter subtree")
            else:
                print("Case 3 not supported")

        self.calculate_balance()
            
    
    def find_pivot(self, new_node):
        current = self.root
        pivot = None
        
        while current is not new_node:
            if current.balance != 0:
                pivot = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right
        
        return pivot
    
    def search(self, key):
        """Search for a key in the BST - iterative version"""
        current = self.root
        
        while current is not None:
            if key == current.key:
                return True
            elif key < current.key:
                current = current.left
            else:
                current = current.right
                
        return False
    
    def calculate_balance(self):
        """Calculate balance factor for each node in the tree"""
        if self.root is None:
            return {}
        
        balance_dict = {}
        self._calculate_heights_and_balance(self.root, balance_dict)
        return balance_dict
    
    def _calculate_heights_and_balance(self, node, balance_dict):
        """Calculate height and balance factor for each node"""
        if node is None:
            return 0
        
        left_height = self._calculate_heights_and_balance(node.left, balance_dict)
        right_height = self._calculate_heights_and_balance(node.right, balance_dict)
        
        balance = right_height - left_height
        node.balance = balance
        balance_dict[node.key] = balance
        
        return max(left_height, right_height) + 1

def main():
    # Test
    tree = BinarySearchTree()
    tree.insert(12) # Root node
    tree.insert(6)  # Should return case 1
    tree.insert(17) # Should return case 2
    tree.insert(8)  # Should return case 1
    tree.insert(10) # Should return case 3

if __name__ == "__main__":
    main()