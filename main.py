import os

def clear_screen():
    os.system("clear" if os.name == "nt" else "clear")
class Player:
    def __init__(self):
        name = ""
        symbol = ""

    def choose_name(self):
        while True:
            name = input("please enter your name (letters only): ")
            if name.isalpha():
                self.name = name
                break
            print("invalid name, please use letters only!")


    def choose_symbol(self):
        while True:
            symbol = input("please enter your symbol(one letter only): ")
            if symbol.isalpha() == True and len(symbol) == 1:
                self.symbol = symbol
                break
            else:
                print("please choose one letter")
class Menu:
    def validate_choice(self):
        while True:
            choice = int(input("Enter your choice 1 or 2: "))
            if choice == 1 or choice == 2:
                return choice

            else:
                print("invalid input!")
    def display_main_menu(self):
        print("welcome to the Game!")
        print("1. start game")
        print("2. quit the game")
        return self.validate_choice()

    def display_endgame_menu(self):
        print("Game Over!")
        print("1. start game")
        print("2. quit the game")
        return self.validate_choice()
class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1,10)]
    def display_board(self):
        for i in  range(0, 9, 3):
            print("|".join(self.board[i:i+3]))
            if i < 6:
                print("-"*5)
    '''def update_board(self):
        while True:
            print("choose position: ")
            self.user_input = input()
            if self.user_input.isalpha() == True:
                continue
            else:
                if Board.board[self.user_input - 1].isalpha() == True:
                    continue
                else:
                    Board.board[self.user_input - 1] = Player.symbol
                    break'''
    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice-1] =symbol
            return True     #??????
        return False
    def is_valid_move(self, choice):
        return self.board[choice-1].isdigit()
    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]
class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0
    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == 1:
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()
    def setup_players(self):
        for player in self.players:
            #print(f"{player + 1} please enter your details")
            player.choose_name()
            player.choose_symbol()

    def play_game(self):
        while True:
            self.player_turn()
            if self.check_win() or self.check_draw():
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break
    def player_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                cell_choice = int(input("choose a cell(1-9): "))
                if 1<=cell_choice<10 and self.board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print("invalid move, try again")
            except ValueError:
                print("Please enter a number between 1 and 9")
        self.switch_player()

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def check_win(self):
        win_combination = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]
        for combo in win_combination:
            if (self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]):
                return True
        return False

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)

    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()

    def quit_game(self):
        print("thank you for playing!")


game = Game()
game.start_game()
