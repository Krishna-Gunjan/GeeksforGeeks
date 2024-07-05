class Solution():

  def verticalWidth(self, root):
    
    if not root:
        return 0
    
    min_max = [0, 0]
    
    minMax(root, 0, min_max)
    
    return min_max[1] - min_max[0] + 1
    
def minMax(self, root, depth, min_max):
    if not root:
        return
    
    if depth < min_max[0]:
        min_max[0] = depth
    if depth > min_max[1]:
        min_max[1] = depth
        
    minMax(root.left, depth - 1, min_max)
    minMax(root.right, depth + 1, min_max)
