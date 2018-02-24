G = [[1,2,3,4,6,7,10],[2,1,3,4,5,6],[3,1,2],[4,1,2],[5,2,6],[6,1,2,5,7,8]]#[[1,2,3], [2,1,3], [3,1,2], [4,5], [5,4]] # a list of lists
n = 6 # number of vertices
k = 4 # number of colours


# (6 1 2 5 7 8)
# (7 1 6 8 9 10)
# (8 6 7 9)
# (9 7 8 10)
# (10 1 7 9)

class Node:
    def __init__(self,val,neighbours,color):
        self.val = val
        self.neighbours = []
        self.color = color
        for neighbour in neighbours:
            self.neighbours.append(neighbour)
            

topo_graph = {}

for vetric in G:
    # create new node and set it color as first color
    new_node = Node(vetric[0],vetric[1::],1)
    if not topo_graph.has_key(new_node.val):
        topo_graph[new_node.val] = new_node.color
        for neighbour in new_node.neighbours:
            if(not topo_graph.has_key(neighbour)):
                topo_graph[neighbour] = new_node.color+1
            else:
                if(topo_graph.get(neighbour) > new_node.color+1):
                    topo_graph[neighbour] = new_node.color+1
    else:
        for neighbour in new_node.neighbours:
            if(new_node.val < neighbour):
                topo_graph[neighbour] = topo_graph.get(new_node.val)+1

for key in topo_graph:
    print(key, " ", topo_graph[key])

# def solve(n, k, G):
#     # write your code here
#     # return solution
#     pass