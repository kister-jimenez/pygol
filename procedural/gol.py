import os
def check_world_dim(world):
    world_row_dim = len(world)
    if( world_row_dim >= 3):
        world_col_dim=len(world[0])
        if (world_col_dim>=3):
            # World is 2D NxM
            for row in world:
                if(world_col_dim != len(row)):
                    print("Inconsistent Matrix Row Dimensions")
                    return False
        else:
            print("World Column dimension should be at least 3 cells")
            return False
    else:
        print("World Row dimension should be at least 3 cells")
        return False
    return True

def display(world):
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

    for row in world:
        for cell in row:
            if (cell==0):
                print(u"\u2B1B", end="") #Dead
            else:
                print(u"\u2B1C", end="") #Alive
        print("")

#def count_neighbors(index, world):

def next(world):
    world_row_dim = len(world)
    world_col_dim = len(world[0])
    new_world=[]
    for row_idx in range(0,world_row_dim):
        new_row=[]
        for col_idx in range(0,world_col_dim):
            cell_state = world[row_idx][col_idx]
            alive_cell_count = 0
            #count alive neighbors
            if (row_idx!=0): #Cell not in first row
                if (col_idx!=0): #Cell not in first col
                    if(world[row_idx-1][col_idx-1]):
                        alive_cell_count += 1
                if (col_idx!=world_col_dim-1): #Cell in last col
                    if(world[row_idx-1][col_idx+1]):
                        alive_cell_count += 1
                if(world[row_idx-1][col_idx]):
                        alive_cell_count += 1
            if (row_idx!=world_row_dim-1): #Cell in last row
                if (col_idx!=0): #Cell not in first col
                    if(world[row_idx+1][col_idx-1]):
                        alive_cell_count += 1          
                if (col_idx!=world_col_dim-1): #Cell in last col
                    if(world[row_idx+1][col_idx+1]):
                        alive_cell_count += 1
                if(world[row_idx+1][col_idx]):
                        alive_cell_count += 1

            if (col_idx!=0): #Cell not in first col
                if(world[row_idx][col_idx-1]):
                    alive_cell_count += 1          
            if (col_idx!=world_col_dim-1): #Cell in last col
                if(world[row_idx][col_idx+1]):
                    alive_cell_count += 1

            if(cell_state):
                if (alive_cell_count<2) or (alive_cell_count>3):
                    cell_state=0
            else:
                if (alive_cell_count==3):
                    cell_state=1
            new_row.append(cell_state)
        new_world.append(new_row)

    return new_world