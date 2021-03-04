import cluster


class AgglomerativeClustering:
    def __init__(self, link, samples):
        """
        This constructor initiates Agglomerative Clustering using parameters and list of clusters
        :param link: link object
        :param samples: list of samples
        """
        self.link = link
        self.samples = samples
        self.clusters = []

    def min_in_distances(self, distances):
        """
        This method finds clusters with min distance between them calculated by link method
        :param distances: matrix of calculated distances
        :return: min_c1, min_c2: two clusters which have min distance between them
        """
        flag = 0
        for i, c1 in enumerate(self.clusters):
            for j, c2 in enumerate(self.clusters):
                if (i == j):
                    continue
                temp_link = self.link.compute(c1, c2, distances)
                flag+=1
                if (flag == 1):
                    min = temp_link
                    min_c1 = c1
                    min_c2 = c2
                if (temp_link < min):
                    min = temp_link
                    min_c1 = c1
                    min_c2 = c2

        return (min_c1, min_c2)

    def update_clusters(self, cluster1, cluster2):
        """
        This method updates the clusters
        :param cluster1
        :param cluster2
        """
        new_cluster = cluster1.merge(cluster2)
        self.clusters.remove(cluster1)
        self.clusters.remove(cluster2)
        self.clusters.insert(new_cluster.id, new_cluster)

    def run(self, max_clusters, distances):
        """
        This method runs the agglomerative clustering algorithm until we reach max clusters
        :param max_clusters: max clusters in list clusters
        :param distances: matrix of calculated distances
        :return: our_cluster: list of sorted clusters (by id)
        """
        for sample in self.samples:
            our_cluster = cluster.Cluster(sample.id, set([sample]))
            self.clusters.append(our_cluster)

        while (len(self.clusters) > max_clusters):
            merging = self.min_in_distances(distances)
            self.update_clusters(merging[0], merging[1])
        our_clusters = self.sort_by_id()
        return our_clusters

    def sort_by_id(self):
        """
        This method sorts the clusters list according to their ids'
        :return: sorted_clusters: the sorted list
        """
        id_list = []
        for c in self.clusters:
            id_list.append(c.id)
        sorted_id_list = sorted(id_list)
        sorted_clusters = []
        for id in sorted_id_list:
            for c in self.clusters:
                if c.id == id:
                    sorted_clusters.append(c)
        return sorted_clusters