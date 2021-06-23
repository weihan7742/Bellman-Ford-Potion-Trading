"""
Author: Ng Wei Han
"""
#%%
class Graph:
    def __init__(self,prices) -> None:
        """
        Initialization of Graph object

        :param prices: Array which each element represents value of 1L of potion

        Best/Worst Time Complexity: O(n)
        n - Number of elements in prices
        Total Space Complexity: O(n)
        Auxiliary Space: O(n)

        """
        self.vertices = [None]*len(prices)
        self.prices = prices

        for i in range(len(prices)):
            vertex = Vertex(i,-prices[i]) # Negate price
            self.vertices[i] = vertex

    def add_edges(self,argv_edges):
        """
        Add edges from vertex to its predecessors.

        :param argv_edges: Array which contains tuple representing predecessor,successor and weight

        Best/Worst Time Complexity: O(n)
        n - Number of elements in argv_edges
        Total Space Complexity: O(n)
        Auxiliary Space: O(1)
        """
        for edge in argv_edges:
            u = edge[0]
            v = edge[1]
            w = edge[2]

            # Add predecessor
            current_edge = Edge(u,v,w)
            current_vertex = self.vertices[v]
            current_vertex.add_predecessor(current_edge)

    def bellman_ford(self,source,max_trades):
        """
        Find the shortest distance from source vertex to every other vertices using Bellman Ford algorithm.

        :param source: An integer representing the starting vertex
        :param max_trades: Maximum number of trades allowed
        :return: An integer which represents the shortest distance

        Best/Worst Time Complexity: O(TM)
        T - Total number of trades available
        M - Value of max_trades
        Total Space Complexity: O(V)
        V - Number of vertices
        Auxiliary Space Complexity: O(V)

        """
        table = [[(float('inf'),0,0) for i in range(2)] for j in range(len(self.prices))] # Use 2-array method

        # Initialize table
        table[source][0] = (self.vertices[source].price,0,1)
        
        max_val = table[source][0][0] # Store final result
        col = 1

        for _ in range(max_trades):
            col = col%2 # Alternate between 1st and 2nd column
            for j in range(len(table)):
                id = j
                current_vertex = self.vertices[id]
                table[id][col] = table[id][(col+1)%2] # Choose next
                v_value = table[id][col][0] # Choose previous

                for edge in current_vertex.predecessors:
                    u = edge.u
                    ratio = edge.w
                    price = self.vertices[id].price
                    u_value,u_trades,u_volume = table[u][(col+1)%2]

                    if u_value == float("inf"): # Not yet discovered
                        continue
                        
                    new_volume = ratio*u_volume
                    new_value = price*new_volume 

                    # Update maximum value
                    if new_value < v_value and new_value < table[id][col][0]:
                        table[id][col] = (new_value,u_trades+1,new_volume)
 
                        if new_value < max_val:
                            max_val = new_value

            col += 1

        return max_val
#%%
class Vertex:
    """
    A vertex class specifically for task 1.
    """
    def __init__(self,id,price):
        """
        Initialization of Vertex object

        :param id: Unique identification of each object
        :param price: An integer representing price of potion

        Best/Worst Time Complexity: O(1)
        Total Space Complexity: O(1)
        Auxiliary Space Complexity: O(1)
        """
        self.id = id
        self.predecessors = []
        self.price = price

    def add_predecessor(self,edge):
        """
        Add predecessor of a Vertex object.

        Best/Worst Time Complexity: O(1)
        Total Space Complexity: O(1)
        Auxiliary Space Complexity: O(1)
        """
        self.predecessors.append(edge)
#%%
class Edge:
    """
    An edge class representing the connection between vertices.
    """
    def __init__(self,u,v,w):
        """
        Initialization of Edge object.

        :param u: An integer representing ID of predecessor
        :param v: An integer representing ID of successor
        :param w: An integer representing the weight

        
        Best/Worst Time Complexity: O(1)
        Total Space Complexity: O(1)
        Auxiliary Space Complexity: O(1)
        """
        self.u = u
        self.v = v
        self.w = w
#%%
def best_trades(prices,starting_potion,max_trades,townspeople):
    """
    Function to obtain the maximum value by trading potions using Bellmand Ford algorithm.

    :param prices: array which each element represents value of 1L of potion
    :param starting_potion: ID of the potion to start with
    :param max_trades: Maximum number of trades allowed
    :param townspeople: List of lists which each interior list represents the trades offered by a
    particular person
    :return: The maximum value of potion

    Best/Worst Time Complexity: O(TM)
    T - Total number of trades available
    M - Value of max_trades
    Total Space Complexity: O(V)
    V - Number of vertices
    Auxiliary Space Complexity: O(V)
    """
    # Initialize graph
    my_graph = Graph(prices)
    edges = []

    # Adding edges
    for trades in townspeople:
        for trade in trades:
            edges.append(trade)
    my_graph.add_edges(edges)
    
    ans = my_graph.bellman_ford(starting_potion,max_trades)    

    return ans*-1