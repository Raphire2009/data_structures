
# GRAPH (Adjacency List)

tree = {
    0: [1, 2],
    1: [0],
    2: [0, 3],
    3: [2]
}


# Part 1: Tree Maximum Depth of Binary Tree


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def buildTree(node, parent):
    root = TreeNode(node)

    children = [n for n in tree[node] if n != parent]

    if len(children) > 0:
        root.left = buildTree(children[0], node)
        if len(children) > 1:
            root.right = buildTree(children[1], node)

            return root

def maxDepth(root):
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1

    # Run Binary Tree part
root = buildTree(0, None)
print("Max Depth:", maxDepth(root))


# PART 2: Graph Find if Path Exists in Graph
    

def hasPath(graph, start, end, visited=None):
    if visited is None:
        visited = set()

        if start == end:
            return True

        visited.add(start)

        for neighbor in graph[start]:
            if neighbor not in visited:
                if hasPath(graph, neighbor, end, visited):
                    return True

                return False

                # Run Graph Path part
print("Path 0 -> 3:", hasPath(tree, 0, 3))  # True
print("Path 1 -> 3:", hasPath(tree, 1, 3))  # True
print("Path 1 -> 99:", hasPath(tree, 1, 99) if 99 in tree else False)  # False