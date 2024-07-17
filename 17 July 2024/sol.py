class Solution:
  
    def createTree(self,parent):
        n = len(parent)
        
        if n == 0:
            return None
            
        tree = {i : Node(i) for i in range(n)}
        root = None
        
        for i in range(n):
            if parent[i] == -1:
                root = tree[i]
            else:
                parent_node = tree[parent[i]]
                
                if not parent_node.left:
                    parent_node.left = tree[i]
                else:
                    parent_node.right = tree[i]
        
        return root
            
