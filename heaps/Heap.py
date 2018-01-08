from math import floor

class BinaryHeap:

    def __str__(self):
        return str(self.items)

    def __init__(self,items):
        self.items = items
        self.build_heap()
        

    def build_heap(self):
        self.heapsize = len(self.items)
        for i in range(floor(len(self.items)/2),0,-1):
            self.heapify(i)

    def heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        A = self.items
        largest = i
        if l < self.heapsize and A[l-1] > A[i-1]:
            largest = l
        else:
            largest = i
        if r < self.heapsize and A[r-1] > A[largest-1]:
            largest = r
        if largest != i:
            A[largest-1], A[i-1] = A[i-1], A[largest-1]
            self.heapify(largest)
    
    def heapsort(self):
        self.build_heap()
        A = self.items
        for i in range(len(A)-1,0,-1):
            A[1], A[i] = A[i], A[1]
            self.heapsize += -1
            self.heapify(1)

    def left(self,i):
        return 2*i

    def right(self,i):
        return (2*i+1)

    def parent(self,i):
        return floor(i/2)

if __name__ == '__main__':
    heap = BinaryHeap([34,24,3,55,14,32,5,3,2])
    print(heap)
    heap.heapsort()
    print(heap)