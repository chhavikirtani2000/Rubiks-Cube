import rubik

def shortest_path(start, end):
    """
    For Question 1, using BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves.

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """
    raise NotImplementedError

def shortest_path_optmized(start, end):
    """
    For Question 2, using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """
    raise NotImplementedError


print("Enter start configuration:")
#start = rubik.input_configuration()

print("Enter end configuration:")
#end = rubik.input_configuration()
start = (6,7,8,0,1,2,9,10,11,3,4,5,12,13,14,15,16,17,18,19,20,21,22,23)
end = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23)
#shortest_path(start, end)
