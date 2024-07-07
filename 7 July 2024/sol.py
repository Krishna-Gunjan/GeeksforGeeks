class Solution:

    def Ancestors(self, root, target):
        
        ancestor = []
        
        def getAncestorNode(root, target, ancestor):
            
            if not root:
                return False
                
            if root.data == target:
                return True
                
            if getAncestorNode(root.left, target, ancestor):
                ancestor.append(root.data)
                return True
            
            if getAncestorNode(root.right, target, ancestor):
                ancestor.append(root.data)
                return True
            
            return False
            
        getAncestorNode(root, target, ancestor)
        return ancestor
