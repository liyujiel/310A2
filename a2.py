# For the assignment, implement basic backtracking search along with the MRV, degree,
# and least constraining value heuristic. In your documentation, make sure that you describe
# your program at a high level and discuss any interesting aspects of your program. Test
# data is in a separate file, asking for a 4-colouring of 10 countries. Run your program on
# this data, as well as trying for a 3-colouring (which will fail). As well, optionally, test your
# program with and without using the heuristics, and report on the improvement (or lack of
# improvement) obtained.


# Function Backtracking-Search(csp) returns solution/failure
# return Recursive-Backtracking({ }, csp)
# Function Recursive-Backtracking(assignment, csp) returns soln/failure
#   if assignment is complete then return assignment
#   var ←Select-Unassigned-Variable(Variables[csp], assignment, csp)
#   for each value in Order-Domain-Values(var, assignment, csp) do
#       if value is consistent with assignment given Constraints[csp] then
#          add {var = value} to assignment
#          result ←Recursive-Backtracking(assignment, csp)
#          if result 6= failure then
#            return result
#          remove {var = value} from assignment
#   return failure

from queue import PriorityQueue

def isComplete(assignment,n):
    if(len(assignment) == n):
        return True
    return False

def pickVertex(unassign):
    color_lens = []
    for index in unassign:
        color_lens.append(len(color[index-1]))
    opt_size = min(color_lens)
    min_poses = [pos for pos,val in enumerate(color_lens) if val == opt_size]
    return  unassign[min_poses[0]]+1

def heuristic(vertex, pos):
    res = 0
    for node in unassign:
        # current node is veterx's neighbour
        if node != vertex and node in G[vertex-1]:
            res  =  res + len(color[vertex-1])
            if pos in color[node-1]:
                res -= 1
    return res


def createColorPq(vertex):
    pq = PriorityQueue()
    for i in range(1,k+1):
        pq.put((heuristic(vertex,i),i))
    return pq

def isConsistant(vertex, curr_color):
    for neighbour in G[vertex-1]:
        if neighbour != G[vertex-1][0]:
            for assignment in assignments:
                if assignment[0] == neighbour and curr_color == assignment[0]:
                    return False
    return True

def removeColor(curr_vertex, curr_color):
    for vertex in G[curr_vertex]:
        if (vertex-1) in set(unassign):
            color[vertex-1].remove(curr_color)

def solve(n, k, G):
    if(isComplete(assignments,n)):
        return assignments

    curr_vertex = pickVertex(unassign)
    # print(curr_vertex)
    colorPq = createColorPq(curr_vertex)

    for _ in range(k):
        curr_color = colorPq.get()[1]
        # print(curr_color)

        if isConsistant(curr_vertex, curr_color):
            # print(curr_vertex)
            assignments.append((curr_vertex,curr_color))
            assigned.append(curr_vertex)
            unassign.remove(curr_vertex)
            # for vertex in G[curr_vertex-1]:
            #     if(vertex in unassign):
            #         # print(color)
            #         color[vertex-1].remove(curr_color)
            removeColor(curr_vertex,curr_color)

            
            ans = solve(n,k,G)

            if ans != []:
                return ans
            
            assignments.remove((curr_vertex,curr_color))
            assigned.remove(curr_vertex)
            for vertex in G[curr_vertex]:
                 if(vertex in unassign):
                    color[vertex].append(curr_color)
            unassign.append(curr_vertex)
    
    return []


# Input 
G = [[1,2,3], [2,1,3], [3,1,2], [4,5], [5,4]] # a list of lists
n = 5  # number of vertices
k = 3  # number of colours

# G = [ [1,2 ,3, 4, 6, 7, 10],[2, 1, 3, 4, 5, 6],[3, 1, 2],[4, 1, 2],[5, 2, 6],[6, 1, 2, 5, 7, 8],[7, 1, 6, 8, 9 ,10],[8, 6, 7, 9],[9, 7, 8, 10],[10, 1, 7, 9]]
# n = len(G)
# k = 4

# inital result assigned nodes, unasigned nodes and assignments for check compelete or not
ans = []
assignments = []
unassign = list(range(1,n+1))
assigned = []
color = []
for i in range(n):
    color.append(list(range(1,k + 1)))

# solve(n,k,G)
print(solve(n,k,G))