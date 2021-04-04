import random


class Matrix:

    # initialise matrix with height m and width n
    def __init__(self, dims, fill=0):
        # save attributes
        self.rows = dims[0]
        self.cols = dims[1]

        # create a new matrix with fill
        self.A = [[(random.random() - 0.5 if fill == "random" else fill) for i in range(self.cols)] for j in range(self.rows)]

    # print matrix
    def __str__(self):
        matrix_string = ''
        for i in range(self.rows):
            matrix_string += ('[' + ''.join( map(lambda x:'{0:8.3f}'.format(x), self.A[i])) + ' ]\n')
        return matrix_string

    # compare two matrices via == operator
    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        if self.rows != other.rows:
            return False
        if self.cols != other.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.A[i][j] != other.A[i][j]:
                    return False
        return True

    # scalar and matrix addition
    def __add__(self, other):
        # create new matrix
        C = Matrix(dims=(self.rows, self.cols), fill=0)

        # check if the other object is of type matrix
        if isinstance(other, Matrix):
            # check size
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError
            # add the elements
            for i in range(self.rows):
                for j in range(self.cols):
                    C.A[i][j] = self.A[i][j] + other.A[i][j]

        # if the other object is a scalar
        elif isinstance(other, (int, float)):
            # add that constant to every element of A
            for i in range(self.rows):
                for j in range(self.cols):
                    C.A[i][j] = self.A[i][j] + other

        return C

    # right scalar and matrix addition
    # since addition is commutative, call __add__(..)
    def __radd__(self, other):
        return self.__add__(other)

    # left subtraction
    # left side: matrix 'self'
    # right side: unknown type 'other'
    def __sub__(self, other):
        C = Matrix(dims=(self.rows, self.cols))

        # if the other object is of type matrix
        if isinstance(other, Matrix):
            # check size
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError
            # calculate result Matrix C
            for i in range(self.rows):
                for j in range(self.cols):
                    C[i, j] = self[i, j] - other[i, j]

        # if the other object is a scalar
        elif isinstance(other, (int, float)):
            for i in range(self.rows):
                for j in range(self.cols):
                    C[i, j] = self[i, j] - other

        # return result matrix
        return C

    # right subtraction
    # left side: unknown type 'other'
    # right side: matrix 'self'
    def __rsub__(self, other):
        C = Matrix(dims=(self.rows, self.cols))

        # if the other object is of type matrix
        if isinstance(other, Matrix):
            # check size
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError
            # calculate result Matrix C
            for i in range(self.rows):
                for j in range(self.cols):
                    C[i, j] = other[i, j] - self[i, j]

        # if the other object is a scalar
        elif isinstance(other, (int, float)):
            for i in range(self.rows):
                for j in range(self.cols):
                    C[i, j] = other - self[i, j]

        # return result matrix
        return C

    # multiplication
    # left side: matrix 'self'
    # right side: unknown type 'other'
    def __mul__(self, other):
        # scalar multiplication if other is of type number
        if isinstance(other, (int, float)):
            C = Matrix(dims=(self.rows, self.cols))
            for r in range(self.rows):
                for c in range(self.cols):
                    C[r, c] = self[r, c] * other
            return C

        if isinstance(other, Matrix):
            # vector multiplication if both self and other are 1D-arrays
            if self.cols == 1 and other.cols == 1 and self.rows > 1 and other.rows > 1:
                # raise ValueError if both matrices are incompatible (when they have different number of rows)
                if self.rows != other.rows:
                    raise ValueError
                # else: compute result matrix C
                C = Matrix(dims=(self.rows, 1))
                for r in range(self.rows):
                    C[r, 0] = self[r, 0] * other[r, 0]
                return C

            # matrix multiplication (matmul) if both self and other are 2D-Arrays
            # e.g. 11x2 * 2x1
            else:
                return self.__matmul__(other)

    # right multiplication
    # left side: unknown
    # right side: matrix
    def __rmul__(self, other):
        # scalar multiplication -> multiplication is commutative -> call __mul__
        if isinstance(other, (int, float)):
            return self.__mul__(other)

        elif isinstance(other, Matrix):
            # vector multiplication (nx1 * nx1) -> multiplication is commutative -> call __mul__
            if self.cols == 1 and other.cols == 1 and self.rows > 1 and other.rows > 1:
                return self.__mul__(other)
            # matrix multiplication (lxm * m*n = l*n)
            return self.__rmatmul__(other)

        else:
            raise ValueError

    # standard matrix multiplication
    def __matmul__(self, other):
        # check if matrices are compatible
        # number of cols of self must be equal to the number of rows in other
        if self.cols != other.rows:
            raise ValueError

        if isinstance(other, Matrix):
            C = Matrix(dims=(self.rows, other.cols))

            for i in range(C.rows):
                for j in range(C.cols):
                    sum = 0

                    for k in range(self.cols):
                        sum += self.A[i][k] * other.A[k][j]

                    C.A[i][j] = sum

            return C

    # get element via []-operator
    def __getitem__(self, key):
        if isinstance(key, tuple):
            i = key[0]
            j = key[1]
            return self.A[i][j]

    # set element via []-opeartor
    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            i = key[0]
            j = key[1]
            self.A[i][j] = value

    # method that transposes a matrix
    def transpose(self):
        C = Matrix(dims=(self.cols, self.rows), fill=0);

        for i in range(self.rows):
            for j in range(self.cols):
                C.A[j][i] = self.A[i][j]

        return C

    # creates a matrix from an input list
    @staticmethod
    def of(input_list):
        if isinstance(input_list, (int, float)):
            C = Matrix(dims=(1, 1), fill=input_list)
        if isinstance(input_list, list):
            C = Matrix(dims=(1, len(input_list)), fill=0)

            for i in range(len(input_list)):
                C[0, i] = input_list[i]

        return C

    # inserts an element into a mx1 matrix (practically a vector)
    def insert(self, index, value):
        if self.cols == 1:
            self.A.insert(index, value)
            self.rows += 1
