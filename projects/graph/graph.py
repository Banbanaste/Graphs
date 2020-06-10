"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}
        self.visited = set()

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()  # set of edges from this vert

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            # add v2 as a neighbor to v1
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex)

        # Create a Set to store visited vertices
        visited = set()

        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()

            # If that vertex has not been visited...
            if v not in visited:
                # Visit it
                print(v)

                # Mark it as visited...
                visited.add(v)

                # Then add all of its neighbors to the back of the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue the starting vertex ID
        s = Stack()
        s.push(starting_vertex)

        # Create a Set to store visited vertices
        visited = set()

        # While the queue is not empty...
        while s.size() > 0:
            # Dequeue the first vertex
            v = s.pop()

            # If that vertex has not been visited...
            if v not in visited:
                # Visit it
                print(v)

                # Mark it as visited...
                visited.add(v)

                # Then add all of its neighbors to the back of the queue
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        print(starting_vertex)
        self.visited.add(starting_vertex)
        for neighbor in self.get_neighbors(starting_vertex):
            if not neighbor in self.visited:
                self.visited.add(neighbor)
                self.dft_recursive(neighbor)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])

        # Create a Set to store visited vertices
        visited = set()

        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()

            current = v[-1]
            # If that vertex has not been visited...
            if current not in visited:

                # Mark it as visited...
                visited.add(current)

                if current is destination_vertex:
                    return v

                # Then add all of its neighbors to the back of the queue
                for next_vert in self.get_neighbors(current):
                    v_copy = list(v)
                    v_copy.append(next_vert)
                    q.enqueue(v_copy)
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty queue and enqueue the starting vertex ID
        s = Stack()
        s.push([starting_vertex])

        # Create a Set to store visited vertices
        visited = set()

        # While the queue is not empty...
        while s.size() > 0:
            # Dequeue the first vertex
            v = s.pop()

            current = v[-1]
            # If that vertex has not been visited...
            if current not in visited:

                # Mark it as visited...
                visited.add(current)

                if current is destination_vertex:
                    return v

                # Then add all of its neighbors to the back of the queue
                for next_vert in self.get_neighbors(current):
                    v_copy = list(v)
                    v_copy.append(next_vert)
                    s.push(v_copy)
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print("*"*10, "\n")
    print(graph.vertices)
    print("*"*10, "\n")
    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print("*"*10, "\n")
    graph.bft(1)
    print("*"*10, "\n")

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("*"*10)
    graph.dft(1)
    graph.dft_recursive(1)
    print("*"*10)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("*"*10, "\n")
    print(graph.bfs(1, 6))
    print("*"*10, "\n")

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("*"*10, "\n")
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
    print("*"*10, "\n")
