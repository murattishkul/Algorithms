import numpy as np

class Heap:
    def __init__(self):
        self.heap = np.empty(0, dtype=int)

    def insert(self, data):
        self.heap = np.append(self.heap, data)
        self.heap_size = self.heap.shape[0]

    def delete(self):
        self.heap_size -= 1

    def element(self, i):
        return self.heap[i]

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def get_heap(self):
        return self.heap

    def get_heap_size(self):
        return self.heap_size

    def parent(self, i):
        assert i < self.heap_size and i >= 0, \
            'Unavailable index i. Index i should be less than the heap size.'
        return int(np.floor((i-1) / 2))

    def left(self, i):
        assert i < self.heap_size or i >= 0, \
            'Unavailable index i. Index i should be less than the heap size.'
        return int(2 * i)+1

    def right(self, i):
        assert i < self.heap_size or i >= 0, \
            'Unavailable index i. Index i should be less than the heap size.'
        return int(2 * i + 1)+1

    def show_heap(self):
        update_line = 0
        step = 2
        for i in range(self.heap_size):
            print(self.heap[i], end=' ')
            if i == update_line:
                update_line += step
                step = step * 2
                print()
        print()

def max_heapify(heap, i):
    l = heap.left(i)
    r = heap.right(i)
    largest = i
    if(l <= heap.get_heap_size() -1 and heap.element(l) > heap.element(largest)):
        largest = l
    if(r <= heap.get_heap_size() - 1 and heap.element(r) > heap.element(largest)):
        largest = r
    if(largest != i):
        heap.swap(i , largest)
        max_heapify(heap, largest)
        

def build_max_heap(heap):
    for i in range(int(np.floor(heap.get_heap_size()/2))-1, -1, -1):
        max_heapify(heap, i)

def heap_sort(heap):
    build_max_heap(heap)
    for i in range(heap.get_heap_size() -1,0,-1):
        heap.swap(i,0)
        heap.delete()
        max_heapify(heap, 0)

def test():
    # Initialize heap structure.
    heap = Heap()

    # Get size of input data.
    heap_size = int(input("Enter the size of input data: "))

    # Randomly generate data and insert it to the heap.
    data = np.random.randint(0, 1e4, size=(heap_size,))
    heap.insert(data)
    
    # Heap sort.
    heap_sort(heap)
    
    # Check whether sorted or not.
    my_heap = heap.get_heap()
    print(my_heap)