from collections import defaultdict

class Solution:
    def printAllDups(self, root):

        duplicates = []
        
        occurence = defaultdict(int)
        
        def node_traversal(node):
            
            if not node:
                return ""
                
            path = str(node.data) + str(node_traversal(node.left)) + str(node_traversal(node.right))
            
            occurence[path] += 1
            
            if occurence[path] == 2:
                duplicates.append(node)

            return path
        
        node_traversal(root)
        
        return duplicates
