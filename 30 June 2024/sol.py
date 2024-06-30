class Solution:
    def delete_node(self, head, x):
 
        if not head:
            return None
            
        current = head
        
        if x == 1:
            head = current.next
            
            if head:
                head.prev = None
                
            return head
            
        for i in range(x - 1):
            current = current.next
            
        if current.next is None:
            current.prev.next = None
            
        else:
          
            if current.prev is not None:
                current.prev.next = current.next
            if current.next is not None:
                current.next.prev = current.prev
              
        return head
