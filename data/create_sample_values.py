import csv
import random
import math


def function(x):
    return 0.25 * math.sin(x) + 0.5


def create_training_values(number_of_samples, start, end):
    with open('sinus_values_training_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        step_size = (end - start) / number_of_samples

        for i in range(number_of_samples):
            x_value = start + i * step_size
            y_value = function(x_value)
            writer.writerow([x_value, y_value])

        file.close()


def create_test_values(number_of_samples, start, end):
    with open('sinus_values_test_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        for i in range(number_of_samples):
            x_value = random.random() * (end - start) + start
            y_value = function(x_value)
            writer.writerow([x_value, y_value])

        file.close()


trainings_values = 10 ** 4
create_training_values(trainings_values, 0, 7)

test_values = 10 ** 3
create_test_values(test_values, 0, 7)
