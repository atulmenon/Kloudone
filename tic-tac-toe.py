class Game:
    def play(self):
        player1 = take_input_player(1)
        player2 = take_input_player(2)
        p1symbol = player1.set_symbol('X')
        print(player1.get_name(),'Symbol',player1.get_symbol())
        p2symbol = player2.set_symbol('O')
        print(player2.get_name(), 'Symbol', player2.get_symbol())
        status = tic_Board.Incomplete
        player1turn =True
        while(status==tic_Board.Incomplete or status==tic_Board.Invalid):
            if (player1turn):
                print(player1.get_name(),"'s trurn")
                player1input = int(input())
                status = tic_Board.move(board,player1input,player1.get_symbol())
                if status!=tic_Board.Invalid:
                    player1turn=False
                    print('player 2 turn')
                    tic_Board.print_board(board)
                else:
                    print('Invalid move try again')
            else:
                player2input = int(input())
                status = tic_Board.move(board,player2input,player2.get_symbol())
                if status!=tic_Board.Invalid:
                    player1turn=True
                    tic_Board.print_board(board)
                else:
                    print('Invalid move try again')

        if status== tic_Board.Player_1_Win:
            print('Player 1 wins')
        elif status== tic_Board.Player_2_Win:
            print("player 2 wins")
        else:
            print('Draws')
class Board:
    def __init__(self ,board):
        self.n= 'X'
        self.p2symbol='O'
        self.count = 0
        self.Player_1_Win = 1
        self.Player_2_Win = 2
        self.Tie = 0
        self.Invalid = -1
        self.Incomplete = 3

        self.board = board

    def print_board(self,board):
        print("-----------")
        print(board[0],'|',board[1],'|',board[2])
        print("-----------")
        print(board[3], '|', board[4], '|', board[5])
        print("-----------")
        print(board[6], '|', board[7], '|', board[8])
        print("-----------")

    def move(self,board,x,symbol):

        if board[x]!=" " :
            return self.Invalid
        self.count+=1
        board[x] = symbol
        if board[0]==board[1]==board[2]==symbol :
            if symbol=='X':
                return self.Player_1_Win
            else:
                return self.Player_2_Win
        if board[4]==board[5]==board[3]==symbol:
            if symbol=='X':
                return self.Player_1_Win
            else:
                return self.Player_2_Win
        if board[6]==board[7]==board[8]==symbol:
            if symbol=='X':
                return self.Player_1_Win
            else:
                return self.Player_2_Win
        if board[0]==board[6]==board[3]==symbol:
            if symbol == "X":
                return self.Player_1_Win
            else:
                return self.Player_2_Win
        if board[4]==board[1]==board[7]==symbol:
            if symbol=='X':
                return self.Player_1_Win
            else:
                return self.Player_2_Win
        if board[2]==board[5]==board[8]==symbol:
            if symbol=='X':
                return self.Player_1_Win
            else:
                return self.Player_2_Win
        if board[0]==board[4]==board[5]==symbol:
            if symbol=='X':
                return self.Player_1_Win
            else:
                return self.Player_2_Win
        if board[2]==board[4]==board[6]==symbol:
            if symbol=='X':
                return self.Player_1_Win
            else:
                return self.Player_2_Win
        if self.count ==9:
            return self.Tie

        return self.Incomplete

class Player:
    def __init__(self,name, symbol):
        self.name=name
        self.symbol = symbol
    def set_symbol(self,symbol):
        if symbol != "":
            self.symbol =symbol
    def get_symbol(self):
        return self.symbol
    def set_name (self,name):
        if name!="":
            self.name = name
    def get_name(self):
        return self.name


def take_input_player(num):
    print("Player",num,"name: ")
    name = input()
    symbol=''
    player = Player(name, symbol)
    return player
board = [" "," "," "," "," "," "," "," "," "]
tic_Board = Board(board)

Game().play()