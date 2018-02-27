# Author: Alex Li
# Student #: 301239152

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

# Check the assignment is complete or not 
def isComplete(assignment,n):
    if len(assignment) == n:
        return True
    return False

def pickVertex(unassign_list):
    color_lens = []
    for index in unassign_list:
        color_lens.append(len(color[index-1]))
    min_size = min(color_lens)
    min_poses = [pos for pos,val in enumerate(color_lens) if val == min_size]
    return unassign_list[min_poses[0]]

  
def heuristic(curr_vertex, temp_color):
    count = 0
    for node in unassign_list:
        if node != curr_vertex and node in G[curr_vertex - 1]:
            count += len(color[node - 1])
            if temp_color in color[node-1]:
                count -= 1
    return count 
 
    
def createColorPq(curr_vertex):
    pq = PriorityQueue()
    for temp_color in range(1,k + 1):
        pq.put((heuristic(curr_vertex, temp_color),temp_color))
    return pq

def isConsistant(curr_vertex, curr_color):
    for neighbour in G[curr_vertex - 1]:
        if neighbour != G[curr_vertex - 1][0]:
            for node in assignment:
                # if neighbour contains same color return false
                if neighbour == node[0] and curr_color == node[1]:
                    return False
    return True

def removeColor(curr_vertex,curr_color):
    for neighbour in G[curr_vertex - 1]:
        if neighbour in unassign_list:
            color[neighbour - 1].remove(curr_color)

def addColor(curr_vertex, curr_color):
    for neighbour in G[curr_vertex - 1]:
        if neighbour in unassign_list:
            color[neighbour - 1].append(curr_color) 
      

def solve(n, k, G):
    # write your code here
    if isComplete(assignment,n):
        return assignment

    curr_vertex = pickVertex(unassign_list)
    colorPq = createColorPq(curr_vertex)
    # print(curr_vertex)
    for _ in range(k):
        curr_color = colorPq.get()[1]
        
        if isConsistant(curr_vertex,curr_color):
            assignment.append((curr_vertex,curr_color))
            assigned_list.append(curr_vertex)
            unassign_list.remove(curr_vertex)
            removeColor(curr_vertex,curr_color)
          
            ans = solve(n,k,G)
            if ans != []:
                return ans

            assignment.remove((curr_vertex,curr_color))
            assigned_list.remove(curr_vertex)
            addColor(curr_vertex,curr_color)
            unassign_list.append(curr_vertex)

    return []


# G = [[1,2,3], [2,1,3], [3,1,2], [4,5], [5,4]] # a list of lists
# n = 5  # number of vertices
# k = 3  # number of colours

G = [[1,2 ,3, 4, 6, 7, 10],[2, 1, 3, 4, 5, 6],[3, 1, 2],[4, 1, 2],[5, 2, 6],[6, 1, 2, 5, 7, 8],[7, 1, 6, 8, 9 ,10],[8, 6, 7, 9],[9, 7, 8, 10],[10, 1, 7, 9]]
n = len(G)
k = 5

# inital result assigned_list nodes, unasigned nodes and assignments for check compelete or not
assignment = []
unassign_list = list(range(1,n+1))
assigned_list = []
color = []
for i in range(n):
    color.append(list(range(1,k + 1)))
ans = []

# solve(n,k,G)
print(solve(n,k,G))
