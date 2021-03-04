
class Cluster:

    def __init__(self, c_id, samples):
        """
         This constructor initiates cluster
         @:param c_id: cluster's id
         @:param samples: cluster's samples
         """
        self.id = c_id
        self.samples = samples

    def merge(self, other):
        """
        This method merges two clusters into one
        @:param other: second cluster
        @:return: new cluster
        """
        new_id = min(self.id, other.id)
        new_samples = self.samples.union(other.samples)
        return Cluster(new_id, new_samples)

    def compute_purity(self):
        """
        This method computes the purity of cluster
        @:return: dominant label and calculated purity
        """
        labels = {'BRCA': 0, 'KIRC': 0, 'PRAD': 0, 'COAD': 0, 'LUAD': 0}
        for sample in self.samples:
            labels[sample.label] +=1
        max_val = max(labels.values())
        max_label = [x for x,y in labels.items() if y == max_val][0]
        rel_labels = 0
        for sample in self.samples:
            if (sample.label == max_label):
                rel_labels +=1
        return (max_label, rel_labels/len(self.samples))

    def __str__(self):
        """
        This method returns string which contains data about cluster
        @:return: string: cluster id, samples, dominant label, purity
        """
        our_samples =[]
        label_purity = self.compute_purity()
        for sample in self.samples:
           our_samples.append(sample.id)
        sorted(our_samples)
        return ('Cluster {0}: {1}, dominant label: {2}, purity: {3}').format(self.id, sorted(our_samples), label_purity[0], label_purity[1])

