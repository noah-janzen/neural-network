from neuralNetwork import NeuralNetwork
import matplotlib.pyplot as plt
import random

# 1 Setup
# ==============================

# initialize neural network
inputNodes = 1
hiddenNodes = 10
outputNodes = 1

learningRate = .4

neuralNetwork = NeuralNetwork(inputNodes, hiddenNodes, outputNodes, learningRate)

# TRAINING DATA
# load training data CSV file into a list
training_data_file = open("data/sinus_values_training_data.csv", 'r')
training_data_list = training_data_file.readlines()
training_data_file.close()

# parse training_data_list
x_training = []
y_training = []
for record in training_data_list:
    x_training.append(float(record.split(',')[0]))
    y_training.append(float(record.split(',')[1]))

# visualize training data
plt.plot(x_training, y_training, '.')
plt.title("Trainingsdaten (" + str(len(x_training)) + " Samples)")
plt.grid()
plt.show()

# TEST DATA
# load the test data CSV file into a list
test_data_file = open("data/sinus_values_test_data.csv", 'r')
test_data_list = test_data_file.readlines()
test_data_file.close()

# parse test_data_list
x_test = []
y_test = []
for record in test_data_list:
    x_test.append(float(record.split(',')[0]))
    y_test.append(float(record.split(',')[1]))

# visualize test data
plt.plot(x_test, y_test, '.', color='green')
plt.title("Testdaten (" + str(len(x_test)) + " Samples)")
plt.grid()
plt.show()


# 2 Train the neural network
# ==============================

acceptable_error = 0.01
error = 1
iteration = 0

# save error over iteration for statistical purposes
iterations = []
errors = []

# shuffle training data
random.shuffle(training_data_list)

while error > acceptable_error:
    # grab next record
    record = training_data_list[iteration % len(training_data_list)]

    # split the record by the ',' semicolon and parse to float values
    values = record.split(',')
    # parse, scale and shift the input
    values[0] = float(values[0]) / 7 * 0.99 + 0.01
    # parse output
    values[1] = float(values[1])

    # train neural network
    neuralNetwork.train([values[0]], [values[1]])

    # 3 Test the neural network…
    # …after x iterations with test data and compute average absolute error
    if iteration % 5000 == 0:
        # scorecard for how well the network performs, initially empty
        scorecard = []
        # save test input and neural output values in lists for plotting later on
        x_test = []
        y_test = []

        for record in test_data_list:
            # split the record by the ',' semicolon
            values = record.split(',')

            # correct answer is second value
            correct_output = float(values[1])

            # scale and shift the input value
            input_value = float(values[0]) / 7 * 0.99 + 0.01
            # save input value in list
            x_test.append(float(values[0]))

            # query the network, query(..) returns data type matrix
            network_output = neuralNetwork.query([input_value])[0, 0]
            # save network output in list
            y_test.append(network_output)

            # compute delta (error) and append it to scorecard
            delta = correct_output - network_output
            scorecard.append(delta)

        # compute average absolute error over all test data records
        average_absolute_error = 0
        for error_value in scorecard:
            error += abs(error_value)
        error /= len(scorecard)

        # save number of iteration and its error for statistic analyze later on
        iterations.append(iteration)
        errors.append(error)

        # print result
        print("iteration: ", iteration, "\terror: ", "%.4f" % error)

    iteration += 1


# Plot test inputs and test outputs
plt.plot(x_test, y_test, '.', color='purple', label='Network output')
# Plot correct sinus function (training values)
plt.plot(x_training, y_training, color='green', label='Training data')

plt.legend()
plt.title("Testergebnisse")
plt.grid()
plt.show()


# Plot error over time/iteration
plt.plot(iterations, errors, color='red')
plt.title("Error over time/iteration")
plt.ylabel("Average absolute error")
plt.xlabel("Number of iteration")
plt.grid()
plt.show()
