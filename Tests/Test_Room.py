import unittest

import main as main


class Test_Room(unittest.TestCase):

    def test_Room_Case_0(self):

        input_filename = "input/Case_Aspi_R_0.txt"
        nx, ny, _, grilleList, robots = main.formatForClean(input_filename)
        piece = main.Cleaning(nx, ny, grilleList, robots)
        self.assertEqual(12, piece.dim)
        self.assertEqual(4, piece.nx)
        self.assertEqual(3, piece.ny)

        self.assertTrue(piece.has_wall(0, "N"))
        self.assertFalse(piece.has_wall(0, "E"))
        self.assertFalse(piece.has_wall(0, "S"))
        self.assertTrue(piece.has_wall(0, "W"))

        self.assertTrue(piece.has_wall(2, "N"))
        self.assertTrue(piece.has_wall(2, "E"))
        self.assertFalse(piece.has_wall(2, "S"))
        self.assertFalse(piece.has_wall(2, "W"))

        self.assertFalse(piece.has_wall(3, "N"))
        self.assertFalse(piece.has_wall(3, "E"))
        self.assertFalse(piece.has_wall(3, "S"))
        self.assertTrue(piece.has_wall(3, "W"))

        self.assertFalse(piece.has_wall(4, "N"))
        self.assertFalse(piece.has_wall(4, "E"))
        self.assertFalse(piece.has_wall(4, "S"))
        self.assertFalse(piece.has_wall(4, "W"))

        self.assertFalse(piece.has_wall(11, "N"))
        self.assertTrue(piece.has_wall(11, "E"))
        self.assertTrue(piece.has_wall(11, "S"))
        self.assertFalse(piece.has_wall(11, "W"))


if __name__ == '__main__':
    unittest.main()
