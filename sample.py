
class Sample:

    def __init__(self, s_id, genes, label):
        """
        This constructor initiates sample
        @:param s_id: sample's id
        @:param genes: sample's list of genes
        @:param label: sample's label
        """
        self.id = s_id
        self.genes = [x for x in genes]
        self.label = str(label)

    def compute_euclidean_distance(self, other):
        """
        This method compute euclidean distance between two genes
        @:param other: second gene
        @:return: calculated distance
        """
        return sum([(my-his)**2 for my, his in zip(self.genes, other.genes)])**0.5
