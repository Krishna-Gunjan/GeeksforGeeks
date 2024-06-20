from math import gcd

class Solution:
    
    def gcd(self, a, b):
        return abs(a) if b == 0 else self.gcd(b, a % b)

    def InternalCount(self, p, q, r):

        p1, p2 = p
        q1, q2 = q
        r1, r2 = r

        area = abs(p1 * (q2 - r2) + q1 * (r2 - p2) + r1 * (p2 - q2))

        boundaryPoints = (self.gcd(abs(q1 - p1), abs(q2 - p2)) +
                          self.gcd(abs(r1 - q1), abs(r2 - q2)) +
                          self.gcd(abs(p1 - r1), abs(p2 - r2)))

        interiorPoints = (area - boundaryPoints + 2) // 2
        return interiorPoints
