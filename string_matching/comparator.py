class Comparator:

    def __init__(self):
        self.count = 0

    def compare(self,p,i,t,j):
        self.count += 1
        try:
            return p[i] == t[j]
        except IndexError:
            raise IndexError(' Exception: i = {}, j = {}'.format(i,j))