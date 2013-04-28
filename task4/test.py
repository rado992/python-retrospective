import unittest

from . import solution


class TicTacHomeworkTest(unittest.TestCase):

    def test_tostring_empty(self):
        b = solution.TicTacToeBoard()
        empty_board = '\n  -------------\n' +\
            '3 |   |   |   |\n' +\
            '  -------------\n' +\
            '2 |   |   |   |\n' +\
            '  -------------\n' +\
            '1 |   |   |   |\n' +\
            '  -------------\n' +\
            '    A   B   C  \n'
        self.assertEqual(empty_board, b.__str__())

    def test_tostring_full(self):
        d = solution.TicTacToeBoard()
        full_board = '\n  -------------\n' +\
            '3 | O | O | X |\n' +\
            '  -------------\n' +\
            '2 | X | X | O |\n' +\
            '  -------------\n' +\
            '1 | O | X | O |\n' +\
            '  -------------\n' +\
            '    A   B   C  \n'

        d["A1"] = 'O'
        d["B1"] = 'X'
        d["A3"] = 'O'
        d["A2"] = 'X'
        d["C2"] = 'O'
        d["C3"] = 'X'
        d["B3"] = 'O'
        d["B2"] = 'X'
        d["C1"] = 'O'

        self.assertEqual(full_board, d.__str__())

    def test_input_format(self):
        o = solution.TicTacToeBoard()
        with self.assertRaises(solution.InvalidKey):
            o['sadads'] = 'X'

        with self.assertRaises(solution.InvalidKey):
            o['Z3'] = 'X'

        with self.assertRaises(solution.InvalidKey):
            o['A4'] = 'X'

        with self.assertRaises(solution.InvalidValue):
            o['A3'] = 'G'

        with self.assertRaises(solution.InvalidValue):
            o['A1'] = None

        with self.assertRaises(solution.InvalidValue):
            o['B2'] = 1

    def test_overwrite_move(self):
        o = solution.TicTacToeBoard()
        with self.assertRaises(solution.NotYourTurn):
            o["A1"] = 'X'
            o["A3"] = 'O'
            o["B2"] = 'X'
            o["A2"] = 'X'

    def test_x_wins(self):
        h = solution.TicTacToeBoard()
        # Horizontal win
        h["A1"] = 'X'
        h["A2"] = 'O'
        h["B1"] = 'X'
        h["A3"] = 'O'
        h["C1"] = 'X'

        self.assertEqual('X wins!', h.game_status())

        # Vertical win
        v = solution.TicTacToeBoard()
        v["A1"] = 'X'
        v["B2"] = 'O'
        v["A2"] = 'X'
        v["B3"] = 'O'
        v["A3"] = 'X'

        self.assertEqual('X wins!', v.game_status())

        # Diagonal win
        d = solution.TicTacToeBoard()
        d["A1"] = 'X'
        d["A2"] = 'O'
        d["B2"] = 'X'
        d["B3"] = 'O'
        d["C3"] = 'X'

        self.assertEqual('X wins!', d.game_status())

    def test_o_wins(self):
        h = solution.TicTacToeBoard()
        # Horizontal win
        h["A1"] = 'O'
        h["A2"] = 'X'
        h["B1"] = 'O'
        h["A3"] = 'X'
        h["C1"] = 'O'

        self.assertEqual('O wins!', h.game_status())

        # Vertical win
        v = solution.TicTacToeBoard()
        v["A1"] = 'O'
        v["B2"] = 'X'
        v["A2"] = 'O'
        v["B3"] = 'X'
        v["A3"] = 'O'

        self.assertEqual('O wins!', v.game_status())

        # Diagonal win
        d = solution.TicTacToeBoard()
        d["A1"] = 'O'
        d["A2"] = 'X'
        d["B2"] = 'O'
        d["B3"] = 'X'
        d["C3"] = 'O'

        self.assertEqual('O wins!', d.game_status())

    def test_draw(self):
        d = solution.TicTacToeBoard()
        d["A1"] = 'O'
        d["B1"] = 'X'
        d["A3"] = 'O'
        d["A2"] = 'X'
        d["C2"] = 'O'
        d["C3"] = 'X'
        d["B3"] = 'O'
        d["B2"] = 'X'
        d["C1"] = 'O'

        self.assertEqual('Draw!', d.game_status())

    def test_game_in_progress(self):
        p = solution.TicTacToeBoard()
        p["A1"] = 'X'
        p["A3"] = 'O'

        self.assertEqual('Game in progress.', p.game_status())

if __name__ == '__main__':
    unittest.main()
