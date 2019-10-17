class Phenotype:
    def __init__(self, weights, input_nodes, hidden_layer_nodes, output_nodes):
        self.weights = weights
        self.input_nodes = input_nodes
        self.hidden_layer_nodes = hidden_layer_nodes
        self.output_nodes = output_nodes

    @staticmethod
    def get_phenotype_from_genotype(genotype, input_nodes, hidden_layer_nodes, output_nodes):
        weights = genotype.weights
        return Phenotype(weights, input_nodes, hidden_layer_nodes, output_nodes)
