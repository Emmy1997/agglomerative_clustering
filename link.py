import abc

class Link:

    @abc.abstractmethod
    def compute(self, cluster, other, distances):
        pass

class SingleLink(Link):
    def compute(self, cluster, other, distances):
        """
        :param cluster
        :param other: second cluster
        :param distances: matrix of calculated distances
        :return: min_distance: minimum distance between the two clusters
        """
        for i, first_sample in enumerate(cluster.samples):
            for j, other_sample in enumerate(other.samples):
                f_id = first_sample.id
                o_id = other_sample.id
                if (i == 0 and j == 0):
                    min_distance = distances[f_id][o_id] if f_id > o_id else distances[o_id][f_id]
                    continue
                curr_distance = distances[f_id][o_id] if f_id > o_id else distances[o_id][f_id]
                if (curr_distance < min_distance):
                    min_distance = curr_distance
        return min_distance


class CompleteLink(Link):
    def compute(self, cluster, other, distances):
        """
         :param cluster
         :param other: second cluster
         :param distances: matrix of calculated distances
         :return: max_distance: maximum distance between the two clusters
         """
        for i, first_sample in enumerate(cluster.samples):
            for j, other_sample in enumerate(other.samples):
                f_id = first_sample.id
                o_id = other_sample.id
                if (i == 0 and j == 0):
                    max_distance = distances[f_id][o_id] if f_id > o_id else distances[o_id][f_id]
                    continue
                curr_distance = distances[f_id][o_id] if f_id > o_id else distances[o_id][f_id]
                if (curr_distance > max_distance):
                    max_distance = curr_distance
        return max_distance