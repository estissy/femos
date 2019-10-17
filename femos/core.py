from random import uniform


def get_random_numbers(quantity, lower_threshold, upper_threshold):
    numbers = []
    for index in range(quantity):
        numbers.append(uniform(lower_threshold, upper_threshold))

    return numbers


def get_number_of_nn_weights(input_nodes, hidden_layers_nodes, output_nodes):
    grouped_nodes = [input_nodes] + hidden_layers_nodes + [output_nodes]

    total = 0
    for index in range(len(grouped_nodes) - 1):
        total += grouped_nodes[index] * grouped_nodes[index + 1]

    return total
