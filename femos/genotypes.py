from math import exp
from random import uniform, gauss

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

    def mutate(self, mean, standard_deviation):

        for index in range(self.weights):
            self.weights[index] = self.weights[index] + gauss(mean, standard_deviation)


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

    def mutate(self, tau1):

        # First mutate current mutation step size
        self.mutation_step_size = self.mutation_step_size * exp(tau1 * gauss(0, 1))

        # Then mutate neural network weights
        for index in range(self.weights):
            self.weights[index] = self.weights[index] + self.mutation_step_size * gauss(0, 1)


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

    def mutate(self, tau1, tau2):

        # First mutate current mutation step sizes
        nonuniform_random_number = gauss(0, 1)
        for index in range(self.mutation_step_sizes):
            self.mutation_step_sizes[index] * exp(tau1 * nonuniform_random_number + tau2 * gauss(0, 1))

        # Then mutate neural network weights
        for index in range(self.weights):
            self.weights[index] = self.weights[index] + self.mutation_step_sizes[index] * gauss(0, 1)


class CorrelatedNStepSizeGenotype:
    pass
