import unittest

import main as main


class Test_Robot(unittest.TestCase):

    def test_Robot_can_move_Game_case_0(self):

        input_filename = "input/Case_Aspi_R_0.txt"
        nx, ny, _, grilleList, robots = main.formatForClean(input_filename)
        piece = main.Cleaning(nx, ny, grilleList, robots)

        r_b = 'B'
        self.assertEqual(3, piece.robots[r_b])

        self.assertTrue(piece.can_move(r_b, "N"))  # North
        self.assertTrue(piece.can_move(r_b, "E"))  # East
        self.assertFalse(piece.can_move(r_b, "S"))  # South
        self.assertFalse(piece.can_move(r_b, "W"))  # West

        r_r = 'R'
        self.assertEqual(6, piece.robots[r_r])

        self.assertFalse(piece.can_move(r_r, "N"))  # North
        self.assertTrue(piece.can_move(r_r, "E"))  # East
        self.assertTrue(piece.can_move(r_r, "S"))  # South
        self.assertFalse(piece.can_move(r_r, "W"))  # West

    def test_Robot_compute_move_Game_case_0(self):
        input_filename = "input/Case_Aspi_R_0.txt"
        r_b = 'B'
        r_r = 'R'

        self.assertEqual(0, main.compute_move(input_filename, r_b, "N"))  # North
        self.assertEqual(5, main.compute_move(input_filename, r_b, "E"))  # East

        self.assertEqual(8, main.compute_move(input_filename, r_r, "E"))  # East
        self.assertEqual(9, main.compute_move(input_filename, r_r, "S"))  # South


if __name__ == '__main__':
    unittest.main()
