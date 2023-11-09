#Somthing to remember is that there has to be a minumum number of coloumns that equals the amount of queens that are on the board

def is_safe(board, row, col, N):
    for i in range(row):
        if board[i][col] ==1:
            return False
        
    for i, j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j] ==1:
            return False
        
    for i, j, in zip(range(row,-1,-1),range(col,N)):
        if board[i][j]==1:
            return False
        
    return True


def solve_nqueens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    if solve_nqueens_util(board,0,N) is False:
        print("No solution exists")
        return False
    print_board(board)


def solve_nqueens_util(board, row, N):
    if row == N:
        return True
    
    for col in range(N):
        if is_safe(board,row,col,N):
            board[row][col] =1
            if solve_nqueens_util(board,row+1,N):
                return True
            board[row][col]=0
    return False



def print_board(board):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))


if __name__ == "main":
    N = 5
    solve_nqueens(N)