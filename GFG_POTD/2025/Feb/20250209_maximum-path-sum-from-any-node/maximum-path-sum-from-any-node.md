# Maximum Path Sum in a Binary Tree

## Approach

If the maximum sum path in a binary tree passes through the root, there are four possible cases to consider:

1. The path consists only the root itself, without involving any children.
2. The path starts at the root and extends downward through its right child, possibly continuing to the bottom of the right subtree.
3. The path starts at the root and extends downward through its left child, possibly continuing the bottom of the left subtree.
4. The path includes the root and spans both the left and right children.
The idea is to keep track of all four paths for each subtree of the tree and pick up the max one in the end. 