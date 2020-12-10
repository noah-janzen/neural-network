from cmath import e
from matrix import Matrix


def sigma(vector):
    C = Matrix(dims=(vector.rows, 1))

    for i in range(vector.rows):
        x = vector[i, 0]
        C[i, 0] = 1 / (1 + e ** (-x))

    return C


def tanh(vector):
    C = Matrix(dims=(vector.rows, 1))

    for i in range(vector.rows):
        x = vector[i, 0]
        C[i, 0] = 1 - 2 / (e ** (2 * x) + 1)

    return C


def linear(vector):
    C = Matrix(dims=(vector.rows, 1))

    for i in range(vector.rows):
        x = vector[i, 0]
        C[i, 0] = x

    return C


# neural network class definition
class NeuralNetwork:

    # initialise the neural network
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        # set number of nodes in each input, hidden, output layer
        self.input_nodes = input_nodes + 1  # + 1 because of bias
        self.hidden_nodes = hidden_nodes + 1  # + 1 because of bias
        self.output_nodes = output_nodes

        # link weight matrices: wih (weights input -> hidden) and who (weights hidden -> output)
        # weights inside the matrices are w_i_j, where link is from node i to node j in the next layer
        self.wih = Matrix(dims=(self.hidden_nodes, self.input_nodes), fill="random")
        self.who = Matrix(dims=(self.output_nodes, self.hidden_nodes), fill="random")

        # learning rate
        self.learning_rate = learning_rate

        pass

    # train the neural network
    def train(self, input_list, target_list):
        # insert bias input to the beginning (position 0) of input_list
        input_list.insert(0, 1.0)

        # convert target_list into own data type matrix
        input_matrix = Matrix.of(input_list)
        target_matrix = Matrix.of(target_list)

        # convert 1xn input_matrix and target_matrix into nx1 matrix (which is practically a vector)
        input_vector = input_matrix.transpose()
        target_vector = target_matrix.transpose()

        # calculate signals into hidden layer
        hidden_inputs = self.wih * input_vector

        # calculate the signals emerging from hidden layer
        hidden_outputs = sigma(hidden_inputs)

        # override hidden neuron with index 0 to bias input 1 each train iteration
        hidden_outputs[0, 0] = 1.0

        # calculate signals into final output layer
        final_inputs = self.who * hidden_outputs

        # calculate the signals emerging from final output layer
        final_outputs = linear(final_inputs)

        # error is the (target - actual)
        output_errors = target_vector - final_outputs

        # hidden layer error is the output_errors, split by weights, recombined at hidden nodes
        hidden_errors = self.who.transpose() * output_errors

        # update the weights for the links between the hidden and output layer
        dwho = self.learning_rate * output_errors * hidden_outputs.transpose()
        self.who += dwho

        # update the weights for the links between the input and hidden layer
        dwih = self.learning_rate * (
                hidden_errors * hidden_outputs * (1.0 - hidden_outputs)) * input_vector.transpose()
        self.wih += dwih

        pass

    # query the neural network
    def query(self, input_list):
        # insert bias input 1 to the beginning (position 0) of input_list
        input_list.insert(0, 1)

        # convert input_list into own data type matrix
        input_matrix = Matrix.of(input_list)

        # convert 1xn input_matrix into nx1 matrix (which is practically a vector)
        input_vector = input_matrix.transpose()

        # calculate signals into hidden layer
        hidden_inputs = self.wih * input_vector

        # calculate the signals emerging from hidden layer
        hidden_outputs = sigma(hidden_inputs)

        # override hidden neuron with index 0 to bias input 1
        hidden_outputs[0, 0] = 1.0

        # calculate signals into final output layer
        final_inputs = self.who * hidden_outputs

        # calculate the signals emerging from output layer
        final_outputs = linear(final_inputs)

        return final_outputs

    pass
