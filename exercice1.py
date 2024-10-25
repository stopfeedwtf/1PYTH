
def new_board(n):
    board = []
    for i in range(n):
        board.append([])
        for j in range(n):
            board[i].append(0)
    return board

def display_board(board, n):
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

def possible_square(board, n, player, i ,j ):
    if i>=n or i < 0 or j>=n or j < 0:
        return False
        
    if board[i][j] == 1 or board[i][j] == 2 :
        return False
    
    if player == 1:
        anti_player=2
    else:
        anti_player=1
    if j-1 >= 0 and board[i][j-1] == anti_player :
        return False
    if j+1 < n and board[i][j+1] == anti_player :
        return False  
    if i-1 >= 0 and  board[i-1][j] == anti_player :
        return False
    if i+1 < n and board[i+1][j] == anti_player :
        return False

    return True

def select_square(board, n, player):
    j=-1
    i=-1
    while not possible_square(board, n, player, i, j):
        i = int(input("Choisissez une case où jouer en position ligne : ")) - 1
        j = int(input("Choisissez une case où jouer en position colonne : ")) - 1
    return (i, j)


def update_board(board, player , i, j):
    board[i][j]=player

def again(board, n, player):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0 and possible_square(board, n, player, i, j):
                return True
    return False

def snort(n):
    player = 2
    board= new_board(n)
    while again(board,n,player):
        player = 1 if player == 2 else 2
        display_board(board,n)
        print("Au tour du joueur : ", player)
        i, j = select_square(board, n, player)
        update_board(board, player, i, j)

    print("Le vainqueur est le joueur", player)


def main():
    snort(int(input("Indiquez le nombre de cases. ")))
    
    

if __name__ == "__main__":
    main()