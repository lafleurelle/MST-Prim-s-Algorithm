class Vertex():
    def __init__(self, key):
        self.key = key
        self.neighbors = {}
    
    def get_neighbors(self):
        return self.neighbors.keys()
    
    def add_neighbor(self, neighbor, weight):
        self.neighbors[neighbor] = weight
        return self
        
    def get_edge(self, neighbor):
        if neighbor in self.get_neighbors():
            return self.neighbors[neighbor]
        
    def print_neighbors(self):
        for i in self.get_neighbors():
            print ('(' + str(self.key) + ',' + str(i) + ',' + str(self.get_edge(i)) + ')')
            
class Graph():
    def __init__(self):
        self.vertices={}
        
    def add_vertex(self, v):
        if v:
            self.vertices[v.key] = v
        return self
        
    def add_edge(self, from_v, to_v, weight):
        if from_v not in self.vertices:
            self.add_vertex(Vertex(from_v))
        if to_v not in self.vertices:
            self.add_vertex(Vertex(to_v))
        self.vertices[from_v].add_neighbor(to_v, weight)
        self.vertices[to_v].add_neighbor(from_v, weight)
        
    def get_vertices(self):
        return self.vertices.keys()
    
    def get_vertex(self, v):
        try:
            return self.vertices[v]
        except KeyError:
            return None
        
    def get_edge(self, from_v, to_v):
        if from_v and to_v in self.get_vertices():
            return self.get_vertex(from_v).get_edge(to_v)
        
    def calculate_graph_weights(self):
        cost = 0
        for i in self.get_vertices():
            nbs = self.get_vertex(i).get_neighbors()
            for j in nbs:
                cost += self.get_edge(i, j)
        return cost//2
    
    def print_graph(self):
        for i in self.vertices:
            self.vertices[i].print_neighbors()
            
class MinHeap():
    def __init__(self):
        self.heap = []
        self.size = 0
        self.key_dict = {}
        
    def insert(self, node):
        self.heap.append(node)
        self.key_dict[node] = self.size
        self.bubble_up(self.size)
        self.size += 1
    
    def extract_root(self):
        self.swap(0, self.size - 1)
        node = self.heap.pop()
        self.key_dict.pop(node)
        self.size -= 1
        self.bubble_down(0)
        return node
        
    def decrease_key(self, node, value):
        ind = self.key_dict[node]
        self.heap[ind] = value
        self.key_dict.pop(node)
        self.key_dict[value] = ind
        self.bubble_up(ind)
        
    def increase_key(self, node, value):
        ind = self.key_dict[node]
        self.heap[ind] = value
        self.key_dict.pop(node)
        self.key_dict[value] = ind
        self.bubble_down(ind)
        
    def swap(self, ind1, ind2):
        tmp = self.heap[ind1]
        self.key_dict[self.heap[ind1]] = ind2
        self.key_dict[self.heap[ind2]] = ind1 
        self.heap[ind1] = self.heap[ind2]
        self.heap[ind2] = tmp               
        
    def bubble_up(self, ind):
        par_ind = (ind - 1)//2
        if (ind > 0) & (self.heap[ind]< self.heap[par_ind]):
            self.swap(ind, par_ind)
            self.bubble_up(par_ind)

    def bubble_down(self, ind):
        ch_ind = self.get_min_child(ind)        
        if ch_ind:
            if self.heap[ind] > self.heap[ch_ind]:
                self.swap(ind, ch_ind)
                self.bubble_down(ch_ind)
                
    
    def get_min_child(self, ind):
        ind1 = 2*ind + 1
        ind2 = 2*ind + 2
        if self.size <= ind1:
            return None
        elif self.size == ind2:
            return ind1
        else:
            if self.heap[ind1] > self.heap[ind2]:
                return ind2
            else:
                return ind1
                
    def get_root(self):
        return self.heap[0]
    
    def get_size(self):
        return self.size
        
    def print_heap(self):
        return print (self.heap, self.key_dict)

def create_graph(path):
    graph = Graph()
    with open(path, 'r') as f:
        for line in f.readlines():
            tmp = list(map(int, line.rstrip().split(' ')))
            if len(tmp) > 2:
                graph.add_edge(tmp[0], tmp[1], tmp[2])
    return graph
    
def build_mst(graph):
    mst = Graph()
    h = MinHeap()
    h.insert((0,1,1))
    vert_dict = dict()
    for j in range(2, len(graph.get_vertices())+1):
        h.insert((1000000,j,1))
        vert_dict[j] = [1000000,1]
    while h.get_size()>0:

        tmp = h.extract_root()
        vert = tmp[1]
        neighbors = [i for i in graph.get_vertex(vert).get_neighbors() if i not in mst.get_vertices()]
        for neighbor in neighbors:
            if vert_dict[neighbor][0] > graph.get_edge(vert,neighbor):
                h.decrease_key((vert_dict[neighbor][0],neighbor, vert_dict[neighbor][1]), (graph.get_edge(vert,neighbor),neighbor, vert))
                vert_dict[neighbor] = [graph.get_edge(vert,neighbor), vert] 
        mst.add_edge(tmp[2], tmp[1], tmp[0])
    return mst
    
if __name__ == "__main__":
    span = build_mst(create_graph('edges.txt'))
    print (span.calculate_graph_weights())
    
