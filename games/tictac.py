# -----------------------------------------------------------------------------
# Name:       tictac
# Purpose:    Implement a game of Tic Tac Toe
#
# Author: Luyan Deng
# -----------------------------------------------------------------------------
'''
Module to implement a Tic-tac-toe game between human player and computer
player. The players take turns marking the spaces in a 3×3 grid. T
he player who succeeds in placing three marks in a horizontal, vertical,
or diagonal row wins the game.
'''
import tkinter
import random

class Game(object):
    '''
    GUI Game class to support a n * n board game

    Argument:
    parent:(tkinter.Tk)  the root window object
    Attribute:
    canvas: (tkinter.Canvas) our drawing canvas

    '''

    # Add your class variables if needed here - square size, etc...)
    # set square size
    sq_size = 100


    def __init__(self, parent):
        parent.title('Tic Tac Toe')
        # save the parent in the object
        self.parent = parent
        self.initialize_game()
        self.draw_board()

    def initialize_game(self):
        """
        Initialize the game
        Parameter: None
        :return: None
        """
        self.board = [None, None, None,
                      None, None, None,
                      None, None, None]
        # map to self.board
        self.map = {(0, 0): 0, (0, 1): 1, (0, 2): 2,
                    (1, 0): 3, (1, 1): 4, (1, 2): 5,
                    (2, 0): 6, (2, 1): 7, (2, 2): 8}
        self.win_combo =((0, 1, 2),
                         (3, 4, 5),
                         (6, 7, 8),
                         (0, 3, 6),
                         (1, 4, 7),
                         (2, 5, 8),
                         (0, 4, 8),
                         (2, 4, 6))

    def draw_board(self):
        """
        draw the game board
        Parameter: None
        Return: the updated object
        """
        restart_frame = tkinter.Frame(self.parent)
        # register it with a geometry manager
        restart_frame.grid()

        # Create the restart button widget
        restart_button = tkinter.Button(self.parent, text='RESTART', width=10,
                                        command=self.restart)
        # register it with a geometry manager
        restart_button.grid(column=0, row=0)
        # Create a canvas widget
        self.canvas = tkinter.Canvas(self.parent,
                                     width=self.sq_size * 3,
                                     height=self.sq_size * 3)
        self.canvas.grid()
        for row in range(3):
            for column in range(3):
                self.canvas.create_rectangle(self.sq_size * column,
                                             self.sq_size * row,
                                             self.sq_size * (column +1),
                                             self.sq_size * (row + 1),
                                             fill='white')
        # register it with a geometry manager
        self.canvas.grid()
        # when the user clicks on the canvas, we invoke self.play
        self.canvas.bind("<Button-1>", self.play)

        # Create a label widget for the win/lose message
        self.message = tkinter.Label(self.parent, text=None)
        # register it with a geometry manager
        self.message.grid()

        return self




    def board_full(self):
        """Check if the board is full or empty"
        Parameter: None
        Return: Boolean Value
        """
        if None in self.board:
            return False
        else:
            return True

    def legal_move(self):
        """
        Check if the move is possible
        Parameter: None
        Return: legal_move(list): a list of possible moves
        """
        legal_move = []
        for i in range(9):
            # check if the square is taken
            if self.board[i] is None:
                # add the square number to the list
                legal_move.append(i)
            else:
                pass # if the square is taken, don't append to the list

        return legal_move

    def pc_move(self):
        """
        Computer player makes move, update the game board
        Parameter: None
        Return: the updated object
        """
        pc_turn= True
        while pc_turn:
            pc_move = random.randint(0, 8)    # random generate a number from 0 to 8
            if pc_move in self.legal_move():  # if the number is a possible move
                self.board[pc_move] = 'O'         # mark O
                self.canvas.itemconfigure(tagOrId=(pc_move+1),fill='cyan')
                pc_turn = False  # exit loop
            else:  # not a possible movie
                continue  # re-do
        return self


    def restart(self):
        """
        invoked the method when the user clicks on the RESTART button
        Return: the updated object
        """
        self.message.destroy()
        self.canvas.destroy()
        self.initialize_game()
        self.draw_board()
        return self

    def sq_num(self,event):
        """
        when the player click a empty square,convert cursor into
        square number
        Parameter: event; click a square
        Return: play_move (int) the square number was clicked
        """
        # convert window coordinate to canvas coordinate
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)

        # map cursor
        play_move = self.map[(y // self.sq_size, x // self.sq_size)]

        return play_move

    def play(self, event):
        """when the human player click on a un-taken square,
        update game board and check game result based on condition
        Parameter: Event: a click on a square
        Return: the updated object
        """
        play_move = self.sq_num(event)

        # check if the square is empty
        if self.board[play_move] is None:
            # if the square is empty mark X for human player
            self.board[play_move] = 'X'
            # fill red color for human player
            click_square = self.canvas.find_closest(event.x, event.y)
            self.canvas.itemconfigure(click_square, fill='magenta')
        else:
            return None
        # if the board is not full, play game
        if not self.board_full():
            self.pc_move()
            self.check_result()
        else: # if the board is full, check the result
            self.check_result()
            self.check_winner()

        return self

    def check_result(self):
        """check game result,win, lose or tie"""

        for row in self.win_combo:
            if self.board[row[0]] == self.board[row[1]]\
                    == self.board[row[2]]is not None:
                winner = self.board[row[0]]
                if winner == 'X':
                    self.message.configure(text='You Won!')

                elif winner == 'O':
                    self.message.configure(text='You Lost!')
                # unbind click so player cannot click on square
                self.canvas.unbind("<Button-1>")

            else:
                if self.board_full():

                    self.message.configure(text="It's a Tie!")
                    self.canvas.unbind("<Button-1>")





    def check_winner(self):
        """
        Check if human or computer wins
        :return: None
        """
        for row in self.win_combo:
            if self.board[row[0]] == self.board[row[1]]\
                    == self.board[row[2]]is not None:
                winner = self.board[row[0]]
                if winner == 'X':
                    self.message.configure(text='You Won!')

                elif winner == 'O':
                    self.message.configure(text='You Lost!')
                self.canvas.unbind("<Button-1>")



def main():
    # Instantiate a root window
    root = tkinter.Tk()
    # Instantiate a Game object
    my_game = Game(root)
    # Enter the main event loop
    root.mainloop()


if __name__ == '__main__':
    main()

