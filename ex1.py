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
            if key < current.key:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
    
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
            return -1
        
        left_height = self._calculate_heights_and_balance(node.left, balance_dict)
        right_height = self._calculate_heights_and_balance(node.right, balance_dict)
        
        balance = right_height - left_height
        balance_dict[node.key] = balance
        
        return max(left_height, right_height) + 1

# Task 3: Generate 1000 random search tasks
def generate_random_tasks():
    """Generate 1000 random search tasks"""
    numbers = list(range(1, 1001))
    tasks = []
    
    # Shuffle the list 1000 times to create different tasks
    for _ in range(1000):
        random.shuffle(numbers)
        tasks.append(numbers.copy())
    
    return tasks

# Task 4: Measure performance and balance
def measure_performance(tree, tasks):
    """Measure search performance for each task and record balance metrics"""
    performance_metrics = []
    
    # Pre-calculate balance once since tree structure isn't changing
    balance_dict = tree.calculate_balance()
    max_abs_balance = max(abs(balance) for balance in balance_dict.values()) if balance_dict else 0
    
    for task in tasks:
        # Measure search time
        start_time = time.time()
        for num in task:
            tree.search(num)
        end_time = time.time()
        search_time = end_time - start_time
        
        performance_metrics.append({
            'search_time': search_time,
            'max_abs_balance': max_abs_balance
        })
    
    return performance_metrics

# Task 5: Generate scatterplot
def generate_scatterplot(metrics):
    """Generate a scatterplot of balance vs. search time"""
    balance_values = [metric['max_abs_balance'] for metric in metrics]
    search_times = [metric['search_time'] for metric in metrics]
    
    plt.figure(figsize=(10, 6))
    plt.scatter(balance_values, search_times, alpha=0.5)
    plt.xlabel('Absolute Balance Value')
    plt.ylabel('Search Time (seconds)')
    plt.title('Relationship Between Tree Balance and Search Performance')
    plt.grid(True)
    plt.savefig('balance_vs_performance.png')
    plt.close()

def main():
    # Create a binary search tree
    bst = BinarySearchTree()
    
    # Insert values in a way that creates an unbalanced tree
    for i in range(1, 1001):
        bst.insert(i)
    
    # Generate random search tasks
    tasks = generate_random_tasks()
    
    # Measure performance
    metrics = measure_performance(bst, tasks)
    
    # Calculate average performance
    avg_search_time = sum(metric['search_time'] for metric in metrics) / len(metrics)
    avg_max_balance = sum(metric['max_abs_balance'] for metric in metrics) / len(metrics)
    
    print(f"Average search time: {avg_search_time:.6f} seconds")
    print(f"Average maximum absolute balance: {avg_max_balance:.2f}")
    
    # Generate scatterplot
    generate_scatterplot(metrics)
    
    print("Scatterplot saved as 'balance_vs_performance.png'")

if __name__ == "__main__":
    main()