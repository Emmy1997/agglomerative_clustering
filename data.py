import pandas
import sample as s


class Data:


    def __init__(self, path):
        """
        This constructor initiates data to dictionary made of file received in path
        @:param path
        """
        df = pandas.read_csv(path)
        self.data = df.to_dict(orient="list")


    def create_samples(self):
        """
        This method creates list of samples out of data
        @:return: our_samples: list of samples
        """
        our_samples = []
        for i in range(len(self.data['sample'])):
            genes_list = []
            for key in self.data.keys():
                if (key == 'sample'):
                    continue
                if (key == 'label'):
                    continue
                genes_list.append(self.data[key][i])
            sample = s.Sample(i, genes_list, self.data['label'][i])
            our_samples.append(sample)
        return our_samples

    def create_distances_matrix(self, samples):
        """
        This method creates matrix where every cell contains calculated distance between 2 samples
        @:param samples: list of all the samples from data
        @:return: distances: the distances matrix
        """
        len_samples = len(samples)
        distances = [[0 for y in range(len_samples)] for x in range(len_samples)]
        i = j = 0
        while (i < len_samples):
            j=0
            while (j < len_samples and j < i) :
                distances[i][j] = samples[i].compute_euclidean_distance(samples[j])
                j+=1
            i+=1
        return distances





