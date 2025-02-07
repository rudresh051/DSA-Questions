# Inorder traversal

Inorder traversal is a method of traversing a binary tree where you visit the nodes in a specific order: left subtree, root node, and then right subtree. This traversal method is particularly useful for binary search trees (BSTs) because it visits the nodes in ascending order, which means you can retrieve the elements in sorted order.

Here's a step-by-step explanation of how inorder traversal works:

1. **Visit the Left Subtree**: Start by traversing the left subtree of the current node recursively.
2. **Visit the Root Node**: Once the left subtree is fully traversed, visit the root node.
3. **Visit the Right Subtree**: Finally, traverse the right subtree of the current node recursively.

This process is repeated for each node in the tree, ensuring that all nodes are visited in the correct order.
