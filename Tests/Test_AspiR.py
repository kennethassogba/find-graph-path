import unittest

import main as main


class Test_AspiR(unittest.TestCase):

    def test_Aspi_R_clean_Aspi_R_case_0(self):

        input_filename = "input/Case_Aspi_R_0.txt"

        path = main.findpath(input_filename)
        self.assertEqual(6, len(path.split()))
        self.assertTrue(main.checkpath(input_filename, path))
        self.assertFalse(main.checkpath(input_filename, 'BN BE BS RS BW'))

        print(" CASE 0: {}".format(path))

    def test_Aspi_R_clean_Aspi_R_case_1(self):

        input_filename = "input/Case_Aspi_R_1.txt"

        path = main.findpath(input_filename)
        self.assertEqual(6, len(path.split()))
        self.assertTrue(main.checkpath(input_filename, path))

        print(" CASE 1: {}".format(path))

    def test_Aspi_R_clean_Aspi_R_case_2(self):

        input_filename = "input/Case_Aspi_R_2.txt"

        path = main.findpath(input_filename)
        self.assertEqual(10, len(path.split()))
        self.assertTrue(main.checkpath(input_filename, path))

        print(" CASE 2: {}".format(path))

    def test_Aspi_R_clean_Aspi_R_case_3(self):

        input_filename = "input/Case_Aspi_R_3.txt"

        path = main.findpath(input_filename)
        self.assertEqual(16, len(path.split()))
        self.assertTrue(main.checkpath(input_filename, path))

        print(" CASE 3: {}".format(path))

    def test_Aspi_R_clean_Aspi_R_case_4(self):

        input_filename = "input/Case_Aspi_R_4.txt"

        path = main.findpath(input_filename)
        self.assertEqual(12, len(path.split()))
        self.assertTrue(main.checkpath(input_filename, path))

        print(" CASE 4: {}".format(path))

    def test_Aspi_R_clean_Aspi_R_case_5(self):

        input_filename = "input/Case_Aspi_R_5.txt"

        path = main.findpath(input_filename)
        self.assertEqual(12, len(path.split()))
        self.assertTrue(main.checkpath(input_filename, path))

        print(" CASE 5: {}".format(path))

    def test_Aspi_R_clean_Aspi_R_case_6(self):

        input_filename = "input/Case_Aspi_R_6.txt"

        path = main.findpath(input_filename)
        self.assertEqual(14, len(path.split()))
        self.assertTrue(main.checkpath(input_filename, path))

        print(" CASE 6: {}".format(path))

    def test_Aspi_R_clean_Aspi_R_case_7(self):

        input_filename = "input/Case_Aspi_R_7.txt"

        path = main.findpath(input_filename)
        self.assertEqual(14, len(path.split()))
        self.assertTrue(main.checkpath(input_filename, path))

        print(" CASE 7: {}".format(path))


if __name__ == '__main__':
    unittest.main()
