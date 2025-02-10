# Tree

It is a type of Data Structure that represent a hierarchial relationship between data elements called nodes.  

![alt text](image.png)

![alt text](image-1.png)

## Binary Tree

It is defined as a tree Data Structure where each node has atmost 2 children

![alt text](image-2.png)

## Understanding Terminologies of Trees
 

### 1. **Node**  
   - A **node** is the fundamental unit of a tree. It contains data and may have references (or pointers) to its child nodes.  
   - Example: In a binary tree, a node can have up to two children.

### 2. **Root**  
   - The **root** is the topmost node of a tree.  
   - It is the only node that does not have a parent.  
   - Example: In a family tree, the oldest known ancestor is the root.

### 3. **Parent**  
   - A **parent** node is one that has one or more child nodes.  
   - Every node (except the root) has exactly one parent.  
   - Example: In a binary tree, if node A has children B and C, then A is the parent of B and C.

### 4. **Child**  
   - A **child** node is a node that has a parent.  
   - It can have its own children (if it’s not a leaf node).  
   - Example: If node A is the parent of node B, then B is the child of A.

### 5. **Leaf**  
   - A **leaf** node is a node that has no children.  
   - It is an endpoint in the tree.  
   - Example: In an organizational chart, employees with no subordinates are leaf nodes.

### 6. **Ancestor**  
   - An **ancestor** of a node is any node that appears above it in the path to the root.  
   - Example: In a family tree, a grandparent and great-grandparent are ancestors.

### 7. **Descendant**  
   - A **descendant** of a node is any node that appears below it in the tree.  
   - Example: A person's children, grandchildren, and great-grandchildren are all descendants.

### 8. **Level**  
   - The **level** of a node represents its depth in the tree.  
   - The **root node is at level 0**, its children are at level 1, their children at level 2, and so on.  
   - Formula: **Level of a node = (Depth of the node)**  

### 9. **Sibling**  
   - **Siblings** are nodes that share the same parent.  
   - Example: In a binary tree, if A is the parent of B and C, then B and C are siblings.

### 10. **Height**  
   - The **height** of a tree is the number of edges on the longest path from the root to a leaf.  
   - **Height of a node** = Number of edges in the longest path from that node to a leaf.  
   - Example: If the longest path from the root to a leaf contains 4 edges, the tree's height is 4.

### 11. **Degree**  
   - The **degree of a node** is the number of its children.  
   - The **degree of a tree** is the maximum degree of any node in the tree.  
   - Example: In a binary tree, the degree of any node is at most 2.

### 12. **Edges**  
   - An **edge** is the connection between two nodes.  
   - A tree with **N nodes has (N-1) edges** because every node (except the root) has exactly one incoming edge.  



Here’s a visual representation of a **Tree Data Structure** illustrating all the concepts:  

```
        A  (Root, Level 0)
       / \
      B   C  (Parent: A, Siblings: B & C, Level 1)
     / \   \
    D   E   F  (Parents: B & C, Level 2)
   / \
  G   H   (Parent: D, Siblings: G & H, Leaf Nodes, Level 3)
```

### Explanation:
1. **Node**: Each letter represents a node (A, B, C, D, E, F, G, H).
2. **Root**: A is the root (topmost node).
3. **Parent**: B is the parent of D and E; C is the parent of F.
4. **Child**: D and E are children of B; F is a child of C.
5. **Leaf**: G, H, E, and F have no children, so they are leaf nodes.
6. **Ancestor**: A is an ancestor of B, C, D, E, F, G, and H.
7. **Descendant**: D, E, F, G, and H are descendants of A.
8. **Level**: A is at level 0, B & C at level 1, D, E, & F at level 2, G & H at level 3.
9. **Sibling**: B and C are siblings; D and E are siblings; G and H are siblings.
10. **Height**: The longest path from A to a leaf (A → B → D → G) has **3 edges**, so the height of the tree is **3**.
11. **Degree**: 
    - Degree of A = 2 (B, C)
    - Degree of B = 2 (D, E)
    - Degree of C = 1 (F)
    - Degree of D = 2 (G, H)
    - Degree of leaf nodes (E, F, G, H) = 0
    - Maximum degree = **2** (Binary Tree)
12. **Edges**: The tree has **7 edges** (A→B, A→C, B→D, B→E, C→F, D→G, D→H).

## How to Create Binary Tree Data structure
