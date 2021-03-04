from data import Data
import sys
import agglomerative_clustering as ag
import link

def main(argv):
    """
    This main method executes algorithm and prints result
    :param argv: path, names of link objects
    """
    dict = Data(argv[1])
    links = argv[2].split(', ')
    links[0] = links[0].replace("_", " ")
    links[1] = links[1].replace("_", " ")
    our_samples = dict.create_samples()
    our_distances = dict.create_distances_matrix(our_samples)
    single_link = link.SingleLink()
    complete_link = link.CompleteLink()
    runner1 = ag.AgglomerativeClustering(single_link, our_samples)
    single_clusters = runner1.run(5, our_distances)
    print('{0}:' .format(links[0]))
    for c in single_clusters:
        s = str(c)
        print(s)
    runner2 = ag.AgglomerativeClustering(complete_link, our_samples)
    complete_clusters = runner2.run(5, our_distances)
    print('\n\n', end='')
    print('{0}:' .format(links[1]))
    for c in complete_clusters:
        s = str(c)
        print(s)



if __name__ == '__main__':
    main(sys.argv)
