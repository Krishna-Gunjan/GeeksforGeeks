def compute(head): 

    string = ""
    
    while head:
        
        string += head.data
        head = head.next
        
    return string == string[::-1]
