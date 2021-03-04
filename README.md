# agglomerative_clustering
**Dataset**

The Dataset used in this clustering is - "TCGA_PANCAN_HiSeq_300", the Dataset contains 300 samples with 20,531 features (every feature represents a gene). There are 5 labels that represents tumors:BRCA, KIRC, COAD, LUAD, PRAD. For further information: https://archive.ics.uci.edu/ml/datasets/gene+expression+cancer+RNA-Seq#.

**Distance method**

In order to compute which of the clusters need to be merged we used euclidean distance. 

**The quality of the algorithm**

The quality of the algorithm is measured  with purity.

**Specifics**
1. The purpose of the algorithm is to cluster the samples according to the features and produce which sample matches a specific type of cancer. 
2. The stop condition: stop clustering when reaching 5 clusters. 
3. We used to types of agglomerative clustering: Single link and Complete link.

**Classes**
1. Cluster: Object That represents a cluster. 
2. Data: In this class we orgenize the data and computing the initial distance matrix.
3. Link: Contains three classes: Link, SingleLink, CompleteLink. 
4. Agglomerative_clustering: In this class we update the clusters and run the algorithm. 
