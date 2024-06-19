class Solution:
    def maxVolume(self, perimeter, area):

        breadth = height = (perimeter - math.sqrt(perimeter**2 - 24 * area)) / 12
    
        length = (perimeter / 4) - 2 * height
        
        return round(length * breadth * height, 2)
