BOARD_COLS = 7
BOARD_ROWS = 6

class Palya():
    def __init__(self):
        self.board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
        self.turns = 0
        self.last_move = [-1, -1] # [r, c]

    def print_board(self):
        print("\n")
        for r in range(BOARD_COLS):
            print(f"  ({r+1}) ", end="")
        print("\n")
        
        
        for r in range(BOARD_ROWS):
            print('|', end="")
            for c in range(BOARD_COLS):
                print(f"  {self.board[r][c]}  |", end="")
            print("\n")

        print(f"{'-' * 42}\n")


    def which_turn(self):
        players = ['X', 'O']
        return players[self.turns % 2]
    
    def in_bounds(self, r, c):
        return (r >= 0 and r < BOARD_ROWS and c >= 0 and c < BOARD_COLS)
    def turn(self, column):
        for i in range(BOARD_ROWS-1, -1, -1):
            if self.board[i][column] == ' ':
                self.board[i][column] = self.which_turn()
                self.last_move = [i, column]

                self.turns += 1
                return True

        return False


    def which_turn(self):
        players = ['X', 'O']
        return players[self.turns % 2]
    
    def in_bounds(self, r, c):
        return (r >= 0 and r < BOARD_ROWS and c >= 0 and c < BOARD_COLS)


    def turn(self, column):
        for i in range(BOARD_ROWS-1, -1, -1):
            if self.board[i][column] == ' ':
                self.board[i][column] = self.which_turn()
                self.last_move = [i, column]

                self.turns += 1
                return True

        return False

    def check_winner(self):
        last_row = self.last_move[0]
        last_col = self.last_move[1]
        last_letter = self.board[last_row][last_col]

        directions = [[[-1, 0], 0, True], 
                      [[1, 0], 0, True], 
                      [[0, -1], 0, True],
                      [[0, 1], 0, True],
                      [[-1, -1], 0, True],
                      [[1, 1], 0, True],
                      [[-1, 1], 0, True],
                      [[1, -1], 0, True]]
        
        for a in range(4):
            for d in directions:
                r = last_row + (d[0][0] * (a+1))
                c = last_col + (d[0][1] * (a+1))

                if d[2] and self.in_bounds(r, c) and self.board[r][c] == last_letter:
                    d[1] += 1
                else:
                    '''
                    Nem keres ebbe az ir??nyba
                    '''
                    d[2] = False

        '''
        Keressen 4-es sort
        '''
        for i in range(0, 7, 2):
            if (directions[i][1] + directions[i+1][1] >= 3):
                self.print_board()
                print(f"{last_letter} a nyertes!")
                return last_letter   

        '''
        Nem tal??lt nyertest
        '''
        return False

def play():
    jatek = Palya()
    
    game_over = False
    while not game_over:
        jatek.print_board()

        '''
        Megk??rj??k a j??t??kost hogy ??rjon be egy sz??mot
        Ha a sz??m nem j?? (P??ld??ul 7 f??l??tti) akkor ??jra k??r egy sz??mot 
        '''
        valid_move = False
        while not valid_move:
            user_move = input(f"{jatek.which_turn()} J??n - k??rlek v??lassz egy oszlopot (1-{BOARD_COLS}) k??z??tt: ")
            try:
                valid_move = jatek.turn(int(user_move)-1)
            except:
                print(f"K??rlek v??lassz 1 sz??mot 1 ??s {BOARD_COLS} k??z??tt")

        '''
        Le??ll??tsa az eg??sz j??t??kot ha van egy nyertes
        '''
        game_over = jatek.check_winner()
        
        '''
        Le??ll??tsa a j??t??kot ha az eredm??ny d??ntetlen 
        '''
        if not any(' ' in x for x in jatek.board):
            print("A v??geredm??ny egyenl?? lett")
            return

if __name__ == '__main__':
    play()