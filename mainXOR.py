from matrix import Matrix
from neuralNetwork import NeuralNetwork
# plot
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# 1)
# number of input, hidden, output nodes
inputNodes = 2
hiddenNodes = 16
outputNodes = 1

# learning rate
learningRate = 0.3

# create instance of a neural network
neuralNetwork = NeuralNetwork(inputNodes, hiddenNodes, outputNodes, learningRate)

# load training data CSV file into a list
training_data_file = open("data/XOR.csv", 'r')
training_data_list = training_data_file.readlines()
training_data_file.close()

# visualize training data
x1_training = []
x2_training = []
z_training = []
for record in training_data_list:
    x1_training.append(float(record.split(',')[0]))
    x2_training.append(float(record.split(',')[1]))
    z_training.append(float(record.split(',')[2]))
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(x1_training, x2_training, z_training, marker='o',  c='r')
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('z')
plt.title("Trainingsdaten")
plt.show()

# 2)
# train the neural network
epochs = 3000

for e in range(epochs):
    for i in range(len(training_data_list)):
        # grab next record with index 0 to length of training_data_list - 1
        record = training_data_list[i]

        # split the record by the ',' semicolon and parse to float values
        values = record.split(',')
        # parse x1 and x2
        input_value = [float(values[0]), float(values[1])]
        # parse output
        target_value = [float(values[2])]

        # train neural network
        neuralNetwork.train(input_value, target_value)

        # print status
        iteration = e * len(training_data_list) + i + 1
        if (iteration % 1000) == 0:
            print("iteration: ", iteration)

# 3) Visualize test data
# test the neural network

# generate test values
step_width = 0.01
x1_test = []
x2_test = []
for i in range(int(1.0 / step_width) + 1):
    x1_test.append(i * step_width)
    x2_test.append(i * step_width)

y_test = []

# go through all records in the test data set
for i in range(len(x1_test)):
    temp = []
    for j in range(len(x2_test)):
        input_list = [x1_test[i], x2_test[j]]
        # query the network
        output = neuralNetwork.query(input_list)

        # append output value
        temp.append(output[0, 0])
    # append temp to y
    y_test.append(temp)

x1_test, x2_test = np.meshgrid(x1_test, x2_test)
y_test = np.array(y_test)

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x1_test, x2_test, y_test)
plt.title("Testdaten")
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('z')
plt.show()

pass
