from random import randint


def get_indices_by_tournament_selection(individual_values, number_of_individuals):
    indices = []

    for index in range(number_of_individuals):
        first_individual_index = randint(0, number_of_individuals - 1)
        second_individual_index = randint(0, number_of_individuals - 1)

        first_individual_value = individual_values[first_individual_index]
        second_individual_value = individual_values[second_individual_index]

        if first_individual_value >= second_individual_value:
            indices.append(first_individual_index)
        else:
            indices.append(second_individual_index)

    return indices
