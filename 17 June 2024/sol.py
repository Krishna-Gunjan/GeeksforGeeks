
class Solution:

    def lieOnSegment(self, p, q, r):

        if min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and min(p[1], r[1]) <= q[1] <= max(p[1], r[1]):
            return "true"
        return "false"
    
    def doIntersect(self, p1, q1, p2, q2):
        #code here
        
        x1, y1 = p1
        x2, y2 = q1
        x3, y3 = p2
        x4, y4 = q2

        if x2 - x1 != 0:
            m1 = (y2 - y1) / (x2 - x1)
            c1 = y1 - m1 * x1
        else:
            m1 = float('inf')
            c1 = x1
        
        if x4 - x3 != 0:
            m2 = (y4 - y3) / (x4 - x3)
            c2 = y3 - m2 * x3
        else:
            m2 = float('inf')
            c2 = x3
        
        if m1 == m2:

            if c1 != c2:
                return "false"
            
            return self.lieOnSegment(p1, p2, q1) or self.lieOnSegment(p1, q2, q1) or self.lieOnSegment(p2, p1, q2) or self.lieOnSegment(p2, q1, q2)
        
        if m1 != float('inf') and m2 != float('inf'):
            x = (c2 - c1) / (m1 - m2)
            y = m1 * x + c1
        elif m1 == float('inf'):
            x = x1
            y = m2 * x + c2
        else:
            x = x3
            y = m1 * x + c1
        
        if (min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2) and
            min(x3, x4) <= x <= max(x3, x4) and min(y3, y4) <= y <= max(y3, y4)):
            return "true"
        
        return "false"
