class Comparator:

    def __init__(self):
        self.count = 0

    def compare(self,p,i,t,j):
        self.count += 1
        return p[i] == t[j]