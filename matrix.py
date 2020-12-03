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

    # ToDo: implement != operator function

    # scalar and matrix addition
    def __add__(self, other):
        # create new matrix
        C = Matrix(dims=(self.rows, self.cols), fill=0)

        # check if the other object is of type matrix
        if isinstance(other, Matrix):
            # Todo: Check if sizes of matrices are the same
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

    # add on the right-hand-side of the matrix
    def __radd__(self, other):
        return self.__add__(other)

    # scalar and matrix subtraction
    def __sub__(self, other):
        C = Matrix(dims=(self.rows, self.cols))

        # check if the other object is of type matrix
        if isinstance(other, Matrix):
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

    # ToDo: Implement
    # subtract on the right-hand-side of the matrix
    def __rsub__(self, other):
        C = Matrix(dims=(self.rows, self.cols))

        for i in range(self.rows):
            for j in range(self.cols):
                C[i, j] = other - self[i, j]

        return C

    # pointwise multiplication
    def __mul__(self, other):
        # create new Matrix
        C = Matrix(dims=(self.rows, self.cols), fill=0)

        # matrix multiplication
        if isinstance(other, Matrix):
            # call matrix multiplication function
            return self.__matmul__(other)

        # scalar multiplication
        if isinstance(other, (int, float)):
            for i in range(self.rows):
                for j in range(self.cols):
                    C.A[i][j] = self.A[i][j] * other

        return C

    # pointwise multiplication right-hand-side of the matrix
    def __rmul__(self, other):
        return self.__mul__(other)

    # standard matrix multiplication
    def __matmul__(self, other):
        # ToDo: Check if matrices are compatible
        # number of cols of A must be equal to the number of rows in B
        if isinstance(other, Matrix):
            C = Matrix(dims=(self.rows, other.cols), fill=0)

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

    # static method that creates a vector of an input array
    @staticmethod
    def of(input_list):
        if isinstance(input_list, (int, float)):
            C = Matrix(dims=(1, 1), fill=input_list)
        if isinstance(input_list, list):
            C = Matrix(dims=(1, len(input_list)), fill=0)

            for i in range(len(input_list)):
                C[0, i] = input_list[i]

        return C