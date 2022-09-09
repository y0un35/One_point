import numpy as np

word = "004006079000000602056092300078061030509000406020540890007410920105000000840600100"
word_list_integers = list(map(int,list(word)))
word_matrix = np.array(word_list_integers,dtype=int)
word_puzzle = word_matrix.reshape(9,9)
print(word_puzzle)
print(20*"*","Solution",20*"*")

# check if the number appears in row/column
def check_row_col(row,column,number):
    global word_puzzle
    # Check in row
    for i in range(0,9):
        if word_puzzle[row][i] == number:
            return False
    
    #Check in column
    for i in range(0,9):
        if word_puzzle[i][column] == number:
            return False
        
    #Check in small grid of 3x3
    row_init = (row // 3) * 3
    column_init = (column // 3) * 3    
    # Loop in square of 3x3
    for i in range(0,3):
        for j in range(0,3):
            if word_puzzle[row_init+i][column_init+j] == number:
                return False
    
    return True

def solution():
    global word_puzzle
    for i in range(0,9):
        for j in range(0,9):
            if word_puzzle[i][j]==0:
                for number in range(1,10):
                    if check_row_col(i,j,number):
                        word_puzzle[i][j] = number
                        solution()
                        word_puzzle[i][j] = 0
                return 
    
    print(np.array(word_puzzle))
print(solution())