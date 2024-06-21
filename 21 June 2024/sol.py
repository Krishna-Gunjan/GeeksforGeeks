class Solution:
    def compareFrac (self, str):
        
        first_fraction, second_fraction= str.split(', ')
        
        if eval(first_fraction) > eval(second_fraction):
            return first_fraction
        
        if eval(first_fraction) < eval(second_fraction):
            return second_fraction
            
        return "equal"
