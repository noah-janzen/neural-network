from matrix import Matrix
from neuralNetwork import NeuralNetwork
import matplotlib.pyplot as plt
import math

# number of input, hidden, output nodes
inputNodes = 1
hiddenNodes = 10
outputNodes = 1

# learning rate
learningRate = 0.9

# create instance of a neural network
neuralNetwork = NeuralNetwork(inputNodes, hiddenNodes, outputNodes, learningRate)

# load the training data CSV file into a list
training_data_file = open("data/sinus_values_training_data.csv", 'r')
training_data_list = training_data_file.readlines()
training_data_file.close()

# visualize training data
x_1 = []
y_1 = []
for record in training_data_list:
    x_1.append(float(record.split(';')[0]))
    y_1.append(float(record.split(';')[1]))
plt.plot(x_1, y_1, '.')
plt.title("Trainingsdaten (" + str(len(x_1)) + " Samples)")
plt.show()

# train the neural network

# epochs is the number of times the training data set is used for training
epochs = 250

for e in range(epochs):
    # go through all records in the training data set
    for record in training_data_list:
        # split the record by the ';' semicolon and parse to float values
        values = record.split(';')

        # parse, scale and shift the input
        values[0] = float(values[0]) #/ 7 * 0.99 + 0.01
        # parse output
        values[1] = float(values[1])

        # train neural network
        neuralNetwork.train(values[0], values[1])

        pass
    pass


# test the neural network

# load the test data CSV file into a list
test_data_file = open("data/sinus_values_test_data.csv", 'r')
test_data_list = test_data_file.readlines()
test_data_file.close()

# visualize test data
x_2 = []
y_2 = []
for record in test_data_list:
    x_2.append(float(record.split(';')[0]))
    y_2.append(float(record.split(';')[1]))
plt.plot(x_2, y_2, '.')
plt.title("Testdaten (" + str(len(x_2)) + " Samples)")
plt.show()

# scorecard for how well the network performs, inititally empty
scorecard = []
x_3 = []
y_3 = []
y_4 = []

# go through all records in the test data set
for record in test_data_list:
    # split the record by the ';' semicolon
    values = record.split(';')
    print(float(values[0]), "input")
    # correct answer is second value
    correct_output = float(values[1])
    print(correct_output, "correct answer")
    # scale and shift the inputs
    input_value = float(values[0]) #/ 7 * 0.99 + 0.01

    # append x value
    x_3.append(float(values[0]))

    # query the network
    output = neuralNetwork.query(input_value)

    # append y value
    y_3.append(output[0, 0])

    # answer of the neural network
    print(format(output[0, 0], ".2f"), "network's answer")
    # append delta to scorecard
    delta = correct_output - output[0, 0]
    scorecard.append(delta)
    print(format(delta, ".2f"), "delta")
    print("---")

average_absolute_error = 0
for error_value in scorecard:
    average_absolute_error += abs(error_value)
average_absolute_error /= len(scorecard)
print("average error: ", average_absolute_error)

print(max(y_3))
print(min(y_3))

plt.plot(x_3, y_3, '.')
x_5 = [0 + x*7/1000 for x in range(1000)]
y_5 = [(0.25 * math.sin(x_5[n]) + 0.5) for n in range(1000)]
plt.plot(x_5, y_5)

plt.title("Ergebnisse: 0,25 * sin(x) + 0,5")
plt.show()

print("ready")