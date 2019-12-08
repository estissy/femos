from os import path, makedirs
from pickle import dump, HIGHEST_PROTOCOL
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


def get_next_population(population, phenotype_strategy, evaluation_strategy, parent_selection_strategy,
                        mutation_strategy, offspring_selection_strategy):
    phenotypes = map(phenotype_strategy, population)
    phenotypes_values = evaluation_strategy(list(phenotypes))

    parent_indices = parent_selection_strategy(phenotypes_values)
    parents = map(lambda parent_index: population[parent_index], parent_indices)

    mutated_parents = map(mutation_strategy, parents)
    offspring = offspring_selection_strategy(population, list(mutated_parents))

    return offspring


def get_population_file_name(number_of_epoch, number_of_prefix_zeros=3, extension=".population"):
    number_of_epoch_digits = len(str(number_of_epoch))
    prefix_zeros = number_of_prefix_zeros - number_of_epoch_digits

    file_name_elements = [0] * prefix_zeros + [number_of_epoch]
    str_file_name_elements = map(str, file_name_elements)

    return ''.join(str_file_name_elements) + extension


def get_evolved_population(initial_population, phenotype_strategy, evaluation_strategy, parent_selection_strategy,
                           mutation_strategy, offspring_selection_strategy, number_of_epochs, backup=None):
    tmp_population = initial_population

    for number_of_epoch in range(number_of_epochs):
        tmp_population = get_next_population(tmp_population, phenotype_strategy, evaluation_strategy,
                                             parent_selection_strategy, mutation_strategy, offspring_selection_strategy)

        if backup is not None:
            number_of_epochs_to_backup = backup[0]

            if number_of_epoch % number_of_epochs_to_backup == 0:
                backup_directory = backup[1]
                makedirs(backup_directory, exist_ok=True)

                number_of_file_name_prefix_zeros = len(str(number_of_epoch)) + 1
                file_extension = backup[2]
                file_name = get_population_file_name(number_of_epoch, number_of_file_name_prefix_zeros, file_extension)
                backup_path = path.join(backup_directory, file_name)

                with open(backup_path, "wb+") as dump_file:
                    dump(tmp_population, dump_file, HIGHEST_PROTOCOL)

    return tmp_population
