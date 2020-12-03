from cmath import e
from matrix import Matrix


# neural network class definition
class NeuralNetwork:

    # initialise the neural network
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        # set number of nodes in each input, hidden, output layer
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        # link weight matrices: wih (weights input -> hidden) and who (weights hidden -> output)
        # weights inside the matrices are w_i_j, where link is from node i to node j in the next layer
        self.wih = Matrix(dims=(self.hidden_nodes, self.input_nodes), fill="random")
        self.who = Matrix(dims=(self.output_nodes, self.hidden_nodes), fill="random")

        # learning rate
        self.learning_rate = learning_rate

        pass

    # should be a static method
    def activation_function(self, vector):
        C = Matrix(dims=(vector.rows, 1), fill=0)

        for i in range(vector.rows):
            x = vector[i, 0]
            C[i, 0] = 1 / (1 + e**(-x))

        return C

    # train the neural network
    def train(self, input_list, target_list):
        # convert input_list and target_list into own data type matrix
        input_matrix = Matrix.of(input_list)
        target_matrix = Matrix.of(target_list)

        # convert 1xn input_matrix and target_matrix into nx1 matrix (which is practically a vector)
        input_vector = input_matrix.transpose()
        target_vector = target_matrix.transpose()

        # calculate signals into hidden layer
        hidden_inputs = self.wih * input_vector

        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)

        # calculate signals into final output layer
        final_inputs = self.who * hidden_outputs

        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)

        # error is the (target - actual)
        output_errors = target_vector - final_outputs

        # hidden layer error is the output_errors, split by weights, recombined at hidden nodes
        hidden_errors = self.who.transpose() * output_errors

        # update the weights for the links between the hidden and output layer
        self.who += self.learning_rate * (output_errors * final_outputs * (1.0 - final_outputs)) * hidden_outputs.transpose()

        # update the weights for the links between the input and hidden layer
        self.wih += self.learning_rate * (hidden_errors * hidden_outputs * (1.0 - hidden_outputs)) * input_vector.transpose()

        pass

    # query the neural network
    def query(self, input_list):
        # convert input_list into own data type matrix
        input_matrix = Matrix.of(input_list)

        # convert 1xn input_matrix into nx1 matrix (which is practically a vector)
        input_vector = input_matrix.transpose()

        # calculate signals into hidden layer
        hidden_inputs = self.wih * input_vector

        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)

        # calculate signals into final output layer
        final_inputs = self.who * hidden_outputs

        # calculate the signals emerging from output layer
        final_outputs = self.activation_function(final_inputs)

        return final_outputs

    pass