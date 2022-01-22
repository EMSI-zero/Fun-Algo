

def ScanDanger(n,board , row , col):
    """Can the board for attacking queens

    Args:
        n (int): board size
        board (list): chessboard
        row (int): row of the given queen
        col (int): column of the given queen
    
    Returns:
        boolean: false if safe, true if not
    """
    
    # top-left direction
    i = row
    j = col
    while(i>=0 and j>=0):
        if(board[i][j] == "Q"):
            return True
        if(board[i][j] == "W"):
            break
        i-= 1
        j-= 1
    
    #top-right
    while(i>= 0 and j < n):
        if(board[i][j] == "Q"):
            return True
        if(board[i][j]== "W"):
            break
        i-= 1
        j+= 1   
    
    # top
    while(i>=0):
        if(board[i][j] == "Q"):
            return True
        if(board[i][j]== "W"):
            break
        i-= 1
        
    return False


def placeQinRow(board, n , row):   
    pass


def placeQ(board, n, row , S):
    """Checks for places possible to place a queen in a row and after
    and obstacle and continues by placing the queens recursively

    Args:
        board (list): chessboard
        n (int): board size
        row (int): given row
        S (int): column of the starting point
    
    Returns:
        boolean: returns if there is a solution by placing the queen in 
        this row and after his obstacle
    """
    
    
    
    # Recursive case:
    
    # Skip the immidiate obstacle- when two obstacles are next to each other    
    if board[row][S] == "W":
        return placeQ(board , n , row, S+1)
    
    #finding the next obstacle
    End = n
    i = S
    while(i< n):
        i+= 1
        if board[row][i] == "W":
            End = i # save the location of the obstacle
            break
    
    # Queen Placement
    Qp = S
    
    hasSolution = False
    
    while(Qp < End):
        if not(ScanDanger(n , board , row , Qp)):                     #Condition: when queen is placed safely
            board[row][Qp] = "Q"
            if(End == n):                                                       # Condition: when there is no obstacle ahead in the row
                hasSolution = placeQ(board , n , row +1 , 0) or hasSolution
            else:                                                               # Condition: when there is and obstacle ahead
                hasSolutionAfterEnd = placeQ(board , n , row , End + 1)
                if not(hasSolutionAfterEnd):                                        # Condition: when the next slice of row has no solution
                    hasSolution = placeQ(board , n , row +1 , 0) or hasSolution
                else:                                                               # Condition: when the next slice has solution
                    hasSolution = hasSolutionAfterEnd or hasSolution
        elif Qp == End-1 and hasSolution == False :                    #Condition: when queen is cant be place until the end of row
            if End < n - 1:                                                     # Condition: When there is and obstacle ahead
                hasSolution = placeQ(board , n , row , End +1)
            elif row + 1 < n:                                                   # Condition: When there is another row ahead
                return placeQ(board , n , row + 1 , 0)
            else:                                                               # Condition: When it's the last cell of the board
                return False
        Qp+=1