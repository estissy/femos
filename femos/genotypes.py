from random import uniform

from .core import get_random_numbers


class SimpleGenotype:

    def __init__(self, weights):
        self.weights = weights

    @staticmethod
    def get_random_genotype(number_of_nn_weights, weight_lower_threshold, weight_upper_threshold):
        weights = get_random_numbers(number_of_nn_weights, weight_lower_threshold, weight_upper_threshold)
        return SimpleGenotype(weights)

    @staticmethod
    def get_random_genotypes(number_of_genotypes, number_of_nn_weights, weight_lower_threshold, weight_upper_threshold):
        genotypes = []
        for index in range(number_of_genotypes):
            genotype = SimpleGenotype.get_random_genotype(number_of_nn_weights, weight_lower_threshold,
                                                          weight_upper_threshold)
            genotypes.append(genotype)

        return genotypes


class UncorrelatedOneStepSizeGenotype:

    def __init__(self, weights, mutation_step_size):
        self.weights = weights
        self.mutation_step_size = mutation_step_size

    @staticmethod
    def get_random_genotype(number_of_nn_weights, weight_lower_threshold, weight_upper_threshold,
                            mutation_step_size_lower_threshold, mutation_step_size_upper_threshold):
        weights = get_random_numbers(number_of_nn_weights, weight_lower_threshold, weight_upper_threshold)
        mutation_step_size = uniform(mutation_step_size_lower_threshold, mutation_step_size_upper_threshold)
        return UncorrelatedOneStepSizeGenotype(weights, mutation_step_size)

    @staticmethod
    def get_random_genotypes(number_of_genotypes, number_of_nn_weights, weight_lower_threshold, weight_upper_threshold,
                             mutation_step_size_lower_threshold, mutation_step_size_upper_threshold):
        genotypes = []
        for index in range(number_of_genotypes):
            genotype = UncorrelatedOneStepSizeGenotype.get_random_genotype(number_of_nn_weights, weight_lower_threshold,
                                                                           weight_upper_threshold,
                                                                           mutation_step_size_lower_threshold,
                                                                           mutation_step_size_upper_threshold)
            genotypes.append(genotype)

        return genotypes


class UncorrelatedNStepSizeGenotype:

    def __init__(self, weights, mutation_step_sizes):
        self.weights = weights
        self.mutation_step_sizes = mutation_step_sizes

    @staticmethod
    def get_random_genotype(number_of_nn_weights, weight_lower_threshold, weight_upper_threshold,
                            mutation_step_size_lower_threshold, mutation_step_size_upper_threshold):
        weights = get_random_numbers(number_of_nn_weights, weight_lower_threshold, weight_upper_threshold)
        mutation_step_sizes = get_random_numbers(number_of_nn_weights, mutation_step_size_lower_threshold,
                                                 mutation_step_size_upper_threshold)
        return UncorrelatedOneStepSizeGenotype(weights, mutation_step_sizes)

    @staticmethod
    def get_random_genotypes(number_of_genotypes, number_of_nn_weights, weight_lower_threshold, weight_upper_threshold,
                             mutation_step_size_lower_threshold, mutation_step_size_upper_threshold):
        genotypes = []
        for index in range(number_of_genotypes):
            genotype = UncorrelatedNStepSizeGenotype.get_random_genotype(number_of_nn_weights, weight_lower_threshold,
                                                                         weight_upper_threshold,
                                                                         mutation_step_size_lower_threshold,
                                                                         mutation_step_size_upper_threshold)
            genotypes.append(genotype)

        return genotypes


class CorrelatedNStepSizeGenotype:
    pass
