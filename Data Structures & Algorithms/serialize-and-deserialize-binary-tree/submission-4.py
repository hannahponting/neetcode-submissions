# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        res = [str(root.val)]
        q = deque([root])
        while q:
            tree = q.popleft()
            if tree.left:
                q.append(tree.left)
                res.append(str(tree.left.val))
            else:
                res.append(str(None))
            
            if tree.right:
                q.append(tree.right)
                res.append(str(tree.right.val))
            else:
                res.append(str(None))
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == '':
            return None
        data = data.split(',')
        tree = TreeNode(int(data[0]))
        q = deque([tree])
        index = 1
        while q:
            node = q.popleft()
            if data[index] != 'None':
                node.left = TreeNode(int(data[index]))
                q.append(node.left)
            index += 1
            if data[index] != 'None':
                node.right = TreeNode(int(data[index]))
                q.append(node.right)
            index += 1
        return tree
