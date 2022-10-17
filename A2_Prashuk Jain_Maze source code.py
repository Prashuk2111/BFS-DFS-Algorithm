import random

maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]]

#  Goal Nodes
Goal_node_1 = [18,23]
Goal_node_2 = [21,2]


#  function to check for out of bounds possibility
def check_next_node(node):
    x = node[0]
    y = node[1]
    
        
    if (x < 0 or x > 24 ):
            return 0

    elif (y < 0 or y > 24):
            return 0

    elif (maze[x][y] == 1):
            return 0

    else:
        return 1


# function to perform bfs OR dfs search algorithm,
def BFS_DFS(BFS_OR_DFS, tie_order):
    cost = 1
    current_node = [0,0]

    open_list = [[11,2]]
    close_list = []

    path = maze

    if tie_order ==  1:
        tie = "lurd"
    else:
        tie = "Ruld"
    
    if BFS_OR_DFS ==  1:
        type = "BFS"
    else:
        type = "DFS"
    

    while((current_node != Goal_node_1) and (current_node != Goal_node_2) ):

 
        current_node = open_list.pop(0)
        x = current_node[0]
        y = current_node[1]
        
        # P is added in the maze to show what all points the path as covered
        path[x][y] = "P"

        if((current_node == Goal_node_1) or (current_node == Goal_node_2)):
            print("the program has successfully run for "+type+" " +tie+"  tie order and total cost is ")
            print(cost)
            print("the goal node searched is")
            print(current_node)
            print("total nodes explored is")
            print(len(close_list))
            # print(path)
            print("path searched is")
            print(path)
            break

        
        left = y-1
        up = x+1
        right = y+1
        down = x-1

        if (tie_order == 1):
            Next_nodes_total = [[x,left], [up,y],[x,right], [down,y]]
        else:
            Next_nodes_total = [[x,right],[up,y],[x,left],[down,y] ]
        

        Next_nodes_checked = []
        #  looping through possible next 4 outcomes to check if they do not lie in out of bounds
        for node in Next_nodes_total:
            node_check_for_constraints = node
             
            #  First two ifs checks for repeated cases, if they lie in close or open list than those nodes arent added
            if node_check_for_constraints in close_list:
                continue

            if node_check_for_constraints in open_list:
                continue

            Tru_false = check_next_node(node)
            if(Tru_false != 0):
                Next_nodes_checked.append(node_check_for_constraints)
        
        if (BFS_OR_DFS == 1):
            #  This is for BFS, basically this appends the new 4 nodes in the end of the open list [LIFO]
            open_list.extend(Next_nodes_checked)
        else:
            #  this one is for DFS, basically it appends the new 4 nodes in the start of the open list (FIFO)
            open_list = Next_nodes_checked + open_list


        # cost is increased by one after every node added
        cost = cost+1 
        close_list.append(current_node)



       

if __name__ == "__main__":

    # First input 1: BFS, 2: DFS
    #  Second input 1: LURD, 2: RULD
    BFS_DFS(1,1)

































































    


    
