"""
Develop and test a Python program that lets two players play tic-tac-toe. Let player 1 be X and player 2
be O. Devise a method for each player to indicate where they wish to place their symbol. The program
should terminate if either there is a winner, or if the game results in a tie. The tic-tac-toe board should be
displayed after every move as shown below.
"""
board={1:" ",2:" ",3:" ",
       4:" ",5:" ",6:" ",
       7:" ",8:" ",9:" ",}
l=[]
def theboard():
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
def default_board():
    print("1|2|3")
    print('-+-+-')
    print("4|5|6")
    print('-+-+-')
    print("7|8|9")
default_board()

def p1wins():
    global x
    x="none"
    if board[1] == board[2] == board[3] == "X":
        x="player 1 wins the game. "
        return x

    elif board[4] == board[5] == board[6] == "X":
        x="player 1 wins the game. "
        return x

    elif board[7] == board[8] == board[9] == "X":
        x="player 1 wins the game. "
        return x

    elif board[1] == board[4] == board[7] == "X":
        x="player 1 wins the game. "
        return x

    elif board[2] == board[5] == board[8] == "X":
        x="player 1 wins the game. "
        return x

    elif board[3] == board[6] == board[9] == "X":
        x="player 1 wins the game. "
        return x

    elif board[1] == board[5] == board[9] == "X":
        x="player 1 wins the game. "
        return x

    elif board[3] == board[5] == board[7] == "X":
        x="player 1 wins the game. "
        return x

def p2wins():
    global y
    y="none"
    if board[1] == board[2] == board[3] == "0":
        y = "player 2 wins the game. "
        return y

    elif board[4] == board[5] == board[6] == "0":
        y = "player 2 wins the game. "
        return y

    elif board[7] == board[8] == board[9] == "0":
        y = "player 2 wins the game. "
        return y

    elif board[1] == board[4] == board[7] == "0":
        y = "player 2 wins the game. "
        return y

    elif board[2] == board[5] == board[8] == "0":
        y = "player 2 wins the game. "
        return y

    elif board[3] == board[6] == board[9] == "0":
        y = "player 2 wins the game. "
        return y

    elif board[1] == board[5] == board[9] == "0":
        y = "player 2 wins the game. "
        return y

    elif board[3] == board[5] == board[7] == "0":
        y = "player 2 wins the game. "
        return y

def game():
    for i in range(4):
        while 1:
            print("player 1 ")
            print("Whice place do you want to place your X")
            choice=int(input())
            if board[choice]==" ":
                board[choice]="X"
                l.append(choice)
                theboard()
                break
            else:
                print("box is filled ")
                continue

        print(p1wins())
        if x=="player 1 wins the game. ":
            break
        while 1:
            print("player 2")
            print("Whice place do you want to place your 0")
            choice1=int(input())
            if board[choice1] == " ":
                board[choice1] = "0"
                l.append(choice1)
                theboard()
                break
            else:
                print("box is filled ")
                continue
        print(p2wins())
        if y=="player 2 wins the game. ":
            break
        if i==3:
            print("final tic tac toe")
            for i in range(1, 10):
                if i not in l:
                    board[i]="X"
                    theboard()
            print(p1wins())
            break

game()