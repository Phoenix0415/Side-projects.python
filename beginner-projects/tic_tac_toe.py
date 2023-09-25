'''
Tic Tac Toe Game
-------------------------------------------------------------
- A classic game of Tic Tac Toe where two players can take turns to mark a spot on the board.
- The game board is a 3x3 grid, and the player who succeeds in placing three of their marks in a
  horizontal, vertical, or diagonal row is the winner.
- It's a two-player game, and players can input their desired spot on the grid.
- The game continues until there is a winner or the board is full (in which case the game is a draw).
'''

import random


class TicTacToe:
    def __init__(self):
        '''Initializes an empty game board.'''
        self.board = []

    def create_board(self):
        '''Creates a 3x3 empty game board.'''
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        '''Randomly decides which player goes first.'''
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        '''Marks the specified spot on the board for the given player.'''
        self.board[row][col] = player

    def has_player_won(self, player):
        '''Checks if the specified player has won the game.'''
        n = len(self.board)
        board_values = set()

        # check rows
        for i in range(n):
            for j in range(n):
                board_values.add(self.board[i][j])

            if board_values == {player}:
                return True
            else:
                board_values.clear()

        # check cols
        for i in range(n):
            for j in range(n):
                board_values.add(self.board[j][i])

            if board_values == {player}:
                return True
            else:
                board_values.clear()

        # check diagonals
        for i in range(n):
            board_values.add(self.board[i][i])
        if board_values == {player}:
            return True
        else:
            board_values.clear()

        board_values.add(self.board[0][2])
        board_values.add(self.board[1][1])
        board_values.add(self.board[2][0])
        if board_values == {player}:
            return True
        else:
            return False

    def is_board_filled(self):
        '''Checks if the game board is full.'''
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        '''Swaps the turn from the current player to the other player.'''
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        '''Displays the current state of the game board.'''
        for row in self.board:
            for item in row:
                print(item, end=' ')
            print()

    def start(self):
        '''Starts the Tic Tac Toe game.'''
        self.create_board()
        player = 'X' if self.get_random_first_player() == 1 else 'O'
        game_over = False

        while not game_over:
            try:
                self.show_board()
                print(f'\nPlayer {player} turn')

                row, col = list(
                    map(int, input(
                        'Enter row & column numbers to fix spot: ').split()))
                print()

                if col is None:
                    raise ValueError(
                        'not enough values to unpack (expected 2, got 1)')

                self.fix_spot(row - 1, col - 1, player)

                game_over = self.has_player_won(player)
                if game_over:
                    print(f'Player {player} wins the game!')
                    continue

                game_over = self.is_board_filled()
                if game_over:
                    print('Match Draw!')
                    continue

                player = self.swap_player_turn(player)

            except ValueError as err:
                print(err)

        print()
        self.show_board()


if __name__ == '__main__':
    '''The entry point of the program. Creates a Tic Tac Toe game instance and starts the game.'''
    tic_tac_toe = TicTacToe()
    tic_tac_toe.start()
