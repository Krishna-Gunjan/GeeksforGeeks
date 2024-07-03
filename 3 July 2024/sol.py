
class Solution:
    def removeAllDuplicates(self, head):
        
        dummy = Node(0)
        dummy.next = head
        prev = dummy
        
        while head:
            
            while head.next and head.data == head.next.data:
                
                head = head.next
                
            if prev.next == head:
                prev = prev.next
                
            else:
                prev.next = head.next
                
            head = head.next
            
        return dummy.next
