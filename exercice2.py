
def newBoard(n):
    Broard = []
    for i in range(n):
        Broard.append([])
        for j in range(n):
            if j == 0 and i < n-1:
                Broard[i].append(2) 
            elif i == n-1 and j > 0 :
                Broard[i].append(1) 
            else:
                Broard[i].append(0)
    return Broard

def displayBoard(board, n):
    for i in range(n):
        print(f"{i+1}", end="")
        if n+1 >= 10 and i+1 < 10:
            print("  |", end=" ")
        else:
            print(" |", end=" ")
        for j in range(n):
            if board[i][j] == 0:
                print(".", end=" ")
            elif board[i][j]== 1:
                print("x", end=" ")
            else:
                print("o", end=" ")
        print()

    print("   ", end=" ")
    if n+1 >= 10 :
        print(" ", end="")
    for i in range (n):
        print("-", end=" ")
    print()

    print("   ", end=" ")
    if n+1 >= 10 :
        print(" ", end="")
    for i in range (n):
        print(i+1, end=" ")
    print()


def possiblePawn(board, n, directions, player, i, j):
    if i >= n or i < 0 or j >= n or j < 0:
        return False
        
    if board[i][j] != player:
        return False
    
    for direction in directions:
        if player == 1 and direction == (1, 0): 
            continue
        if player == 2 and direction == (0, -1): 
            continue
        
        new_i = i + direction[0]
        new_j = j + direction[1]

        if player == 1  and new_i == -1:
            return True
        if player == 2  and new_j == n:
            return True
        if new_i >= 0 and new_i < n and new_j >= 0 and new_j < n and board[new_i][new_j] == 0:
            return True

    return False

def selectPawn(board, n, directions, player):    
    i = -1
    j = -1
    while not possiblePawn(board, n, directions, player, i, j):
        i = int(input("Choisissez une case où jouer.")) - 1
        j = int(input("Choisissez une case où jouer.")) - 1
    return i, j

def possibleMove(board, n, directions, player, i, j, m):
    
    if i >= n or i < 0 or j >= n or j < 0:
        return False
    
    if m < 0 or m > 4:
        return False
        
    if board[i][j] != player:
        return False
    
    if player == 1 and directions[m] == (1, 0): 
        return False
    if player == 2 and directions[m] == (0, -1): 
        return False
    
    new_i = i + directions[m][0]
    new_j = j + directions[m][1]

    if player == 1 and new_i == -1:
        return True
    if player == 2 and new_j == n:
        return True
    if new_i >= 0 and new_i < n and new_j >= 0 and new_j < n and board[new_i][new_j] == 0:
        return True
    
    return False

def selectMove(board, n, directions, player, i, j):
    m=-2
    while not possibleMove(board, n, directions, player, i, j, m):
        m = int(input("Choisissez une direction où jouer.")) - 1
    return m

def move(board, n, directions, player, i, j, m):
    board[i][j]=0
    new_i=i+directions[m][0]
    new_j=j+directions[m][1]

    if player == 1  and new_i == -1:
        return 
    if player == 2  and new_j == n:
        return 
    
    board[new_i][new_j]=player

def win(board, n, directions, player):
    for i in range(n):
        for j in range(n):
            if board[i][j] == player and possiblePawn(board, n, directions, player, i, j):
                    return False
    return True

def dodgem(n):  
    board = newBoard(n)
    directions =((-1,0),(0,1),(1,0),(0,-1))
    player = 1
    displayBoard(board, n)
    while not win(board, n, directions, player):            
        print("Au tours du player : ", player)
        i, j = selectPawn(board, n, directions, player)
        m = selectMove(board, n, directions, player, i, j)
        move(board, n, directions, player, i, j, m)
        displayBoard(board, n)
        if not win(board, n, directions, player):
            player = 1 if player == 2 else 2


    print("Le vainqueur est le player ", player)

def main():
    dodgem(int(input("Indiquez le nombre de cases. ")))
    
    

if __name__ == "__main__":
    main()