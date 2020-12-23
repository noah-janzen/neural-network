from neuralNetwork import NeuralNetwork
import matplotlib.pyplot as plt
import numpy as np

# 1 Setup
# ==============================

# initialize neural network
inputNodes = 2
hiddenNodes = 16
outputNodes = 1

learningRate = 0.3

neuralNetwork = NeuralNetwork(inputNodes, hiddenNodes, outputNodes, learningRate)

# TRAINING DATA
# load training data CSV file into a list
training_data_file = open("data/XOR.csv", 'r')
training_data_list = training_data_file.readlines()
training_data_file.close()

# parse training_data_list
x1_training = []
x2_training = []
y_training = []
for record in training_data_list:
    x1_training.append(float(record.split(',')[0]))
    x2_training.append(float(record.split(',')[1]))
    y_training.append(float(record.split(',')[2]))

# visualize training data
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(x1_training, x2_training, y_training, marker='o', c='r')
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')
plt.title("Trainingsdaten")
plt.show()

# 2 Train the neural network
# ==============================

epochs = 3000

for epoch in range(epochs):
    for record in training_data_list:
        # split the record by the ',' semicolon and parse to float values
        values = record.split(',')
        # parse x1 and x2
        input_vector = [float(values[0]), float(values[1])]
        # parse output
        target_value = [float(values[2])]

        # train neural network
        neuralNetwork.train(input_vector, target_value)

    # print status
    if ((epoch + 1) % 500) == 0:
        print("epoch: ", epoch + 1)

# 3 Test the neural network
# ==============================

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

# Visualize test result
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
