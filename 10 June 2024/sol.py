class Solution:
    
    def __init__(self):
        self.order = ['!', '#', '$', '%', '&', '*', '?', '@', '^']

    def matchPairs(self, n, nuts, bolts):

        nuts_count = [0] * len(self.order)
        bolts_count = [0] * len(self.order)

        for nut in nuts:
            index = self.get_index(nut)
            if index != -1:
                nuts_count[index] += 1

        for bolt in bolts:
            index = self.get_index(bolt)
            if index != -1:
                bolts_count[index] += 1

        index = 0
        for i in range(len(self.order)):
            while nuts_count[i] > 0:
                nuts[index] = self.order[i]
                index += 1
                nuts_count[i] -= 1

        index = 0
        for i in range(len(self.order)):
            while bolts_count[i] > 0:
                bolts[index] = self.order[i]
                index += 1
                bolts_count[i] -= 1

    def get_index(self, ch):
        for i, char in enumerate(self.order):
            if char == ch:
                return i
        return -1

if __name__ == '__main__':
    sol = Solution()
