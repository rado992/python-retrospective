import re


class TicTacToeBoard:

    def __init__(self):
        self.fields = {"A": {1: " ", 2: " ", 3: " "},
                       "B": {1: " ", 2: " ", 3: " "},
                       "C": {1: " ", 2: " ", 3: " "}}
        self.status = 'Game in progress.'
        self.previous = " "
        self.game_won = False

    def __str__(self):
        return '\n  -------------\n' +\
               '3 | ' + self.fields['A'][3] +\
               ' | ' + self.fields['B'][3] +\
               ' | ' + self.fields['C'][3] + ' |\n' +\
               '  -------------\n' +\
               '2 | ' + self.fields['A'][2] +\
               ' | ' + self.fields['B'][2] +\
               ' | ' + self.fields['C'][2] + ' |\n' +\
               '  -------------\n' +\
               '1 | ' + self.fields['A'][1] +\
               ' | ' + self.fields['B'][1] +\
               ' | ' + self.fields['C'][1] + ' |\n' +\
               '  -------------\n' +\
               '    A   B   C  \n'

    def __getitem__(self, key):
        field = self.fields[key[0]][int(key[1])]
        return None if field == ' ' else field

    def __setitem__(self, key, value):
        if not bool(re.search(r'^[ABC][123]$', key)):
            raise InvalidKey()
        if value != "X" and value != "O":
            raise InvalidValue()
        if self.previous == value:
            raise NotYourTurn()
        if self.fields[key[0]][int(key[1])] != ' ':
            raise InvalidMove()
        self.fields[key[0]][int(key[1])] = value
        self.previous = value

    def check_win(self, player):

        if self.game_won:
            return False

        for i in ['A', 'B', 'C']:
            self.win = True
            for j in range(1, 4):
                if self.fields[i][j] != player:
                    self.win = False
            if self.win:
                self.game_won = True

        for j in range(1, 4):
            self.win = True
            for i in ['A', 'B', 'C']:
                if self.fields[i][j] != player:
                    self.win = False
            if self.win:
                self.game_won = True

        self.win = True
        for i, j in zip(('A', 'B', 'C'), (1, 2, 3)):
            if self.fields[i][j] != player:
                self.win = False
        if self.win:
            self.game_won = True

        self.win = True
        for i, j in zip(('A', 'B', 'C'), (3, 2, 1)):
            if self.fields[i][j] != player:
                self.win = False
        if self.win:
            self.game_won = True

        return self.game_won

    def board_full(self):
        for i in ['A', 'B', 'C']:
            for j in range(1, 4):
                if self.fields[i][j] == " ":
                    return False
        return True

    def game_status(self):
        if self.check_win('X'):
            self.status = 'X wins!'
        elif self.check_win('O'):
            self.status = 'O wins!'
        elif self.board_full() and not self.game_won:
            self.status = 'Draw!'
        return self.status


class InvalidMove(Exception):
    def __init__(self, message=""):
        self.message = message


class InvalidKey(Exception):
    def __init__(self, message=""):
        self.message = message


class InvalidValue(Exception):
    def __init__(self, message=""):
        self.message = message


class NotYourTurn(Exception):
    def __init__(self, message=""):
        self.message = message
