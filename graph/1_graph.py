"""
    Graph --> Abstract data type (ADT)

    # u ---> v   (directed graph)
    # u <--> v   (undirected graph)

    cycle in a graph (enclosed structure in a graph)
    u --- v 
    |     |         undirected cyclic graph 3 cycles are there in (min one cycle present) cyclic else Acyclic 
    w --- z
     \   /
       x

    path in a graph (contains a lot of nodes and each of them is reachable.)
    degree of graph (undirected graph degree of graph means numbers of edges attached to a node)

    total degree of a graph is always twice the numbers of edges. deg(u) = 2, deg(w) = 2 etc...

    --------------------------------------------
    ### Directed Graphs
    --------------------------------------------

    indegree -> indegree(node) numbers of incoming edges.
    outdegree -> outdegree(node) numbers of outgoing edges.

    Edge weight -> A graph may have weight assigned on its edges. (cost of the edge.) if weight not assigned then it is unit weight i.e 1. cos t of the route.

    1. nodes n, 2. edges m ==> edge(u, v)
    
    --------------------------------------------
    ## storage options 
    --------------------------------------------

    1. Adjacency Matrix --> 
        A. 2D matrix of size (n+1) * (n+1) if nodes are 1-indexed.
        B. for unweighted graphs, marks 1 for edge -> e(u, v) = 1.
        C. for weighted graphs, store the weight instead of 1.
        D. Directed: only matrix[u][v] = 1, undirected: matrix[u][v] = 1, matrix[v][u] = 1.
    
        Pros:
            1. simple to implement, 2. Fast O(1) lookup to check if an edge exists.
        cons:
            1. Uses O(n^2) Space which can be wasteful for sparse graphs

    2. Adjancency List -->
        A. create an array of list of size (n+1)
        B. for each edge (u, v) add:
            undirected: list[u].add(v) and list[v].add(u)
            directed: list[u].add(v) only
        C. for weighted : store pairs (v, w)

        Pros:
            1. space effiecient: O(2E) for undirected and O(1E) for directed
            2. Good for sparse graphs.
        Cons:
            1. Checking if a specific edge exists is O(k) where k is the number for neighbors.

    --------------------------------------------
    ## Dense vs Sparse Graph
    --------------------------------------------
    --> Dense graph has many edges close to the maximum possible
    a. for undirected graph with n nodes -> max possible edges = n*(n-1)/2
    b. for directed graph with n node -> max possible edges = n*(n-1)*2
    c. graph has edges close to the maximum (>50% of possible edges) it is considered as dense. ( social networks )

    --> sparse graph has very few edges compared to the maximum possible.

    Operations on Graphs -> 
        1. Depth first search traversal. 
            A. Explores as far as possible along each branch before backtracking.
            B. Uses a stack (or recursion).
        2. Breadth first search traversal.
            A. Explores all neighbors of a vertex before moving to the next level.
            B. Uses a queue.

"""


        