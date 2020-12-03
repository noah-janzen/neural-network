import unittest
from matrix import Matrix


class TestMatrix(unittest.TestCase):

    # ToDo: Implement method
    def setUp(self):
        self.matrix_a = Matrix(dims=(3, 2))
        self.fill_b_value = 5
        self.matrix_b = Matrix(dims=(2, 3), fill=self.fill_b_value)
        self.matrix_c = Matrix(dims=(3, 2), fill="random")
        self.fill_d_value = -4
        self.matrix_d = Matrix(dims=(2, 3), fill=self.fill_d_value)
        self.fill_e_value = 3
        self.matrix_e = Matrix(dims=(2, 3), fill=self.fill_e_value)
        self.matrix_f = Matrix(dims=(2, 3), fill=self.fill_e_value)
        self.scalar_a = 11
        self.scalar_b = -5
        self.fill_g_value = -3.3
        self.matrix_g = Matrix(dims=(3, 2), fill=self.fill_g_value)
        pass

    # ToDo:
    def tearDown(self):
        pass

    def test_constructor_fill_constant_number(self):
        self.assertEqual(self.matrix_a.rows, 3)
        self.assertEqual(self.matrix_a.cols, 2)

        self.assertAlmostEqual(self.matrix_a[0, 0], 0)
        self.assertAlmostEqual(self.matrix_a[0, 1], 0)

        self.assertAlmostEqual(self.matrix_b[0, 0], 5)
        self.assertAlmostEqual(self.matrix_b[1, 1], 5)

    def test_constructor_fill_random_numbers(self):
        self.assertEqual(self.matrix_c.rows, 3)
        self.assertEqual(self.matrix_c.cols, 2)

        self.assertGreaterEqual(self.matrix_c[0, 0], -0.5)
        self.assertLessEqual(self.matrix_c[0, 0], +0.5)
        self.assertNotEqual(self.matrix_c[0, 0], self.matrix_c[1, 1])

        self.assertGreaterEqual(self.matrix_c[0, 1], -0.5)
        self.assertLessEqual(self.matrix_c[0, 1], +0.5)

        self.assertGreaterEqual(self.matrix_c[2, 1], -0.5)
        self.assertLessEqual(self.matrix_c[2, 1], +0.5)

    def test_add_scalar(self):
        addition_matrix = self.matrix_b + self.scalar_a
        expected_result_value = self.fill_b_value + self.scalar_a

        self.assertEqual(addition_matrix[0, 0], expected_result_value)
        self.assertEqual(addition_matrix[0, 1], expected_result_value)
        self.assertEqual(addition_matrix[0, 2], expected_result_value)
        self.assertEqual(addition_matrix[1, 0], expected_result_value)
        self.assertEqual(addition_matrix[1, 1], expected_result_value)
        self.assertEqual(addition_matrix[1, 2], expected_result_value)

        addition_matrix = self.matrix_b + self.scalar_b
        expected_result_value = self.fill_b_value + self.scalar_b

        self.assertEqual(addition_matrix[0, 0], expected_result_value)
        self.assertEqual(addition_matrix[0, 1], expected_result_value)
        self.assertEqual(addition_matrix[0, 2], expected_result_value)
        self.assertEqual(addition_matrix[1, 0], expected_result_value)
        self.assertEqual(addition_matrix[1, 1], expected_result_value)
        self.assertEqual(addition_matrix[1, 2], expected_result_value)

    def test_add_matrix(self):
        addition_matrix = self.matrix_b + self.matrix_d
        expected_result_value = self.fill_b_value + self.fill_d_value

        self.assertEqual(addition_matrix[0, 0], expected_result_value)
        self.assertEqual(addition_matrix[1, 1], expected_result_value)

        addition_matrix = self.matrix_b + self.matrix_e
        expected_result_value = self.fill_b_value + self.fill_e_value

        self.assertEqual(addition_matrix[0, 0], expected_result_value)
        self.assertEqual(addition_matrix[1, 1], expected_result_value)

    def test_radd_scalar(self):
        addition_matrix = self.scalar_a + self.matrix_b
        expected_result_value = self.fill_b_value + self.scalar_a

        self.assertEqual(addition_matrix[0, 0], expected_result_value)
        self.assertEqual(addition_matrix[0, 1], expected_result_value)
        self.assertEqual(addition_matrix[0, 2], expected_result_value)
        self.assertEqual(addition_matrix[1, 0], expected_result_value)
        self.assertEqual(addition_matrix[1, 1], expected_result_value)
        self.assertEqual(addition_matrix[1, 2], expected_result_value)

        addition_matrix = self.scalar_b + self.matrix_b
        expected_result_value = self.fill_b_value + self.scalar_b

        self.assertEqual(addition_matrix[0, 0], expected_result_value)
        self.assertEqual(addition_matrix[0, 1], expected_result_value)
        self.assertEqual(addition_matrix[0, 2], expected_result_value)
        self.assertEqual(addition_matrix[1, 0], expected_result_value)
        self.assertEqual(addition_matrix[1, 1], expected_result_value)
        self.assertEqual(addition_matrix[1, 2], expected_result_value)

    def test_equal(self):
        # wrong size
        self.assertFalse(self.matrix_a == self.matrix_b)
        # wrong values
        self.assertFalse(self.matrix_b == self.matrix_d)
        # wrong data type
        self.assertFalse(self.matrix_a == self.scalar_b)
        # correct test
        self.assertTrue(self.matrix_e == self.matrix_f)

    def test_str(self):
        expected_string = "[   5.000   5.000   5.000 ]\n"
        expected_string += "[   5.000   5.000   5.000 ]\n"

        self.assertEqual(self.matrix_b.__str__(), expected_string)

    def test_get_item(self):
        self.assertEqual(self.matrix_b[0, 0], self.fill_b_value)
        self.assertEqual(self.matrix_d[1, 1], self.fill_d_value)
        self.assertEqual(self.matrix_e[1, 2], self.fill_e_value)

    def test_set_item(self):
        val = -14.4
        self.matrix_a[0, 0] = val
        self.matrix_a[1, 1] = val
        self.assertEqual(self.matrix_a[0, 0], val)
        self.assertEqual(self.matrix_a[1, 1], val)

    def test_sub_scalar(self):
        result_matrix = self.matrix_b - self.scalar_a
        result_value = self.fill_b_value - self.scalar_a

        # is matrix_b unchanged?
        self.assertEqual(self.matrix_b[0, 0], self.fill_b_value)
        self.assertEqual(self.matrix_b[1, 1], self.fill_b_value)

        # is result matrix correct?
        self.assertEqual(result_matrix[0, 0], result_value)
        self.assertEqual(result_matrix[1, 1], result_value)

    def test_sub_matrix(self):
        result_matrix = self.matrix_b - self.matrix_d
        result_value = self.fill_b_value - self.fill_d_value

        # are both matrices unchanged?
        self.assertEqual(self.matrix_b[0, 0], self.fill_b_value)
        self.assertEqual(self.matrix_b[1, 1], self.fill_b_value)
        self.assertEqual(self.matrix_d[0, 0], self.fill_d_value)
        self.assertEqual(self.matrix_d[1, 1], self.fill_d_value)

        # is result matrix correct?
        self.assertEqual(result_matrix[0, 0], result_value)
        self.assertEqual(result_matrix[1, 2], result_value)

    def test_rsub_scalar(self):
        result_matrix = self.scalar_a - self.matrix_b
        result_value = self.scalar_a - self.fill_b_value

        # is matrix_b unchanged?
        self.assertEqual(self.matrix_b[0, 0], self.fill_b_value)
        self.assertEqual(self.matrix_b[1, 1], self.fill_b_value)

        self.assertEqual(self.matrix_b[0, 0], self.fill_b_value)
        self.assertEqual(result_matrix[0, 0], result_value)
        self.assertEqual(result_matrix[1, 2], result_value)

    def test_mul_scalar(self):
        actual_result_matrix = self.matrix_b * self.scalar_a
        expected_result_value = self.fill_b_value * self.scalar_a

        # check values
        self.assertEqual(actual_result_matrix[0, 0], expected_result_value)
        self.assertEqual(actual_result_matrix[1, 1], expected_result_value)

    # tests matrix multiplication, too.
    def test_mul_matrix(self):
        actual_result_matrix = self.matrix_b * self.matrix_g
        expected_result_value = self.fill_b_value * self.fill_g_value * 3

        # check size of matrix
        self.assertEqual(actual_result_matrix.cols, self.matrix_g.cols)
        self.assertEqual(actual_result_matrix.rows, self.matrix_b.rows)

        # check values
        self.assertEqual(actual_result_matrix[0, 0], expected_result_value)
        self.assertAlmostEqual(actual_result_matrix[1, 1], expected_result_value)

    def test_rmul_scalar(self):
        actual_result_matrix = self.scalar_a * self.matrix_b
        expected_result_value = self.scalar_a * self.fill_b_value

        # check values
        self.assertEqual(actual_result_matrix[0, 0], expected_result_value)
        self.assertEqual(actual_result_matrix[1, 1], expected_result_value)

    def test_transpose(self):
        actual_result_matrix = self.matrix_c.transpose()
        expected_result_matrix_cols = self.matrix_c.rows
        expected_result_matrix_rows = self.matrix_c.cols

        # check right size of result matrix
        self.assertEqual(actual_result_matrix.rows, expected_result_matrix_rows)
        self.assertEqual(actual_result_matrix.cols, expected_result_matrix_cols)

        # check right values of result matrix
        for i in range(actual_result_matrix.rows):
            for j in range(actual_result_matrix.cols):
                self.assertEqual(actual_result_matrix[i, j], self.matrix_c[j, i])

    def test_static_of(self):
        input_list = [12.12, 11.1, -0.3]
        actual_result_matrix = Matrix.of(input_list)

        # check correct size
        self.assertEqual(actual_result_matrix.rows, 1)
        self.assertEqual(actual_result_matrix.cols, len(input_list))

        # check correct values
        for i in range(len(input_list)):
            self.assertEqual(actual_result_matrix[0, i], input_list[i])


if __name__ == '__main__':
    unittest.main()
