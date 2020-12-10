from matrix import Matrix
from neuralNetwork import NeuralNetwork
import matplotlib.pyplot as plt
import math
import random

# 1)
# number of input, hidden, output nodes
inputNodes = 1
hiddenNodes = 10
outputNodes = 1

# learning rate
learningRate = .4

# create instance of a neural network
neuralNetwork = NeuralNetwork(inputNodes, hiddenNodes, outputNodes, learningRate)

# load training data CSV file into a list
training_data_file = open("data/sinus_values_training_data.csv", 'r')
training_data_list = training_data_file.readlines()
training_data_file.close()

# visualize training data
x_training = []
y_training = []
for record in training_data_list:
    x_training.append(float(record.split(',')[0]))
    y_training.append(float(record.split(',')[1]))
plt.plot(x_training, y_training, '.')
plt.title("Trainingsdaten (" + str(len(x_training)) + " Samples)")
plt.show()

# load the test data CSV file into a list
test_data_file = open("data/sinus_values_test_data.csv", 'r')
test_data_list = test_data_file.readlines()
test_data_file.close()

# visualize test data
x_test = []
y_test = []
for record in test_data_list:
    x_test.append(float(record.split(',')[0]))
    y_test.append(float(record.split(',')[1]))
plt.plot(x_test, y_test, '.')
plt.title("Testdaten (" + str(len(x_test)) + " Samples)")
plt.show()

# 2)
# train the neural network
acceptable_error = 0.01
error = 1
iterations = []
errors = []
iteration = 0

# shuffe training data
random.shuffle(training_data_list)

while error > acceptable_error:
    # grab next record with index 0 to length of training_data_list - 1
    record = training_data_list[iteration % len(training_data_list)]

    # split the record by the ',' semicolon and parse to float values
    values = record.split(',')
    # parse, scale and shift the input
    values[0] = float(values[0]) / 7 * 0.99 + 0.01
    # parse output
    values[1] = float(values[1])

    # train neural network
    neuralNetwork.train([values[0]], [values[1]])

    iteration += 1

    # test neural network after 1000 iterations and compute error
    if iteration % 1000 == 0:
        # test
        scorecard = []

        # go through all records in the test data set
        for record in test_data_list:
            # split the record by the ',' semicolon
            values = record.split(',')

            # correct answer is second value
            correct_output = float(values[1])

            # scale and shift the inputs
            input_value = float(values[0]) / 7 * 0.99 + 0.01

            # query the network
            output = neuralNetwork.query([input_value])

            # append delta to scorecard
            delta = correct_output - output[0, 0]
            scorecard.append(delta)

        # compute error
        average_absolute_error = 0
        for error_value in scorecard:
            error += abs(error_value)
        error /= len(scorecard)

        # append to list
        iterations.append(iteration)
        errors.append(error)

        # print result
        print("iteration: ", iteration, "\terror: ", error)

# 3) Visualize the test data
# test the neural network

# scorecard for how well the network performs, initially empty
scorecard = []
x_3 = []
y_3 = []

# go through all records in the test data set
for record in test_data_list:
    # split the record by the ',' semicolon
    values = record.split(',')

    # correct answer is second value
    correct_output = float(values[1])

    # scale and shift the inputs
    input_value = float(values[0]) / 7 * 0.99 + 0.01

    # append x value
    x_3.append(float(values[0]))

    # query the network
    output = neuralNetwork.query([input_value])

    # append y value
    y_3.append(output[0, 0])

    # append delta to scorecard
    delta = correct_output - output[0, 0]
    scorecard.append(delta)

average_absolute_error = 0
for error_value in scorecard:
    average_absolute_error += abs(error_value)
average_absolute_error /= len(scorecard)
print("average error: ", average_absolute_error)

plt.plot(x_3, y_3, '.')

x_4 = [0 + x * 7 / 1000 for x in range(1000)]
y_4 = [(math.sin(x_4[n])) for n in range(1000)]
plt.plot(x_4, y_4)

plt.title("Ergebnisse: sin(x)")
plt.show()

# print error over time/iteration
plt.plot(iterations, errors)
plt.show()

print("ready")
