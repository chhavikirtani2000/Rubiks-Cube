import rubik
from collections import deque
import time
start_time = time.time()
def shortest_path(start, end):
    """
    For Question 1, using BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves.

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """

    q = deque()
    visited = {}
    path = {}

    visited[start] = 1
    path[start] = []
    q.append(start)
    
    while(q):
        curr = q[0]
        q.popleft()
        for i in rubik.quarter_twists:
            p = rubik.perm_apply(curr,i)
            if(visited.has_key(p)==False):
                visited[p]=1
                path[p] = path[curr]+[rubik.quarter_twists_names[i]]
                #print(rubik.quarter_twists_names[i])
                q.append(p)
                if(p==end):
                    return path[p]
        
    return []



def shortest_path_optmized(start, end):
    q1 = deque()
    q2 = deque()
    visited1 = {}
    visited2 = {}
    path1 = {}
    path2 = {}

    visited1[start] = 1
    visited2[end]=1
    path1[start] = []
    path2[end] = []
    q1.append(start)
    q2.append(end)
    while(q1 and q2):
        curr1 = q1[0]
        curr2 = q2[0]
        q1.popleft()
        q2.popleft()
        for i in rubik.quarter_twists:
            p1 = rubik.perm_apply(curr1,i)
            p2 = rubik.perm_apply(curr2,i)
            if(visited1.has_key(p1)==False):
                visited1[p1]=1
                path1[p1] = path1[curr1]+[rubik.quarter_twists_names[i]]
                #print(rubik.quarter_twists_names[i])
                q1.append(p1)
                if(visited2.has_key(p1)==True):
                    return path1[p1]+path2[p1]
            if(visited2.has_key(p2)==False):
                visited2[p2]=1
                path2[p2] = path2[curr2]+[rubik.quarter_twists_names[rubik.perm_inverse(i)]]
                #print(rubik.quarter_twists_names[i])
                q2.append(p2)
                if(visited1.has_key(p2)==True):
                    return path1[p2]+path2[p2]
        
    return []
    """
    For Question 2, using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """
    raise NotImplementedError


#print("Enter start configuration:")
#start = rubik.input_configuration()

#print("Enter end configuration:")
#end = rubik.input_configuration()
start = (6, 7, 8, 20, 18, 19, 3, 4, 5, 16, 17, 15, 0, 1, 2, 14, 12, 13, 10, 11, 9, 21, 22, 23)
end = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)
print(shortest_path(start, end))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(shortest_path_optmized(start, end))
print("--- %s seconds ---" % (time.time() - start_time))

