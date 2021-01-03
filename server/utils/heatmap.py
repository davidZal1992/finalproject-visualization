from utils import inchlib_clust_dev as inchlib_clust
def create_heatmap_json(data,**kwargs):
    row_distance = kwargs.pop('row_distance')
    row_linkage = kwargs.pop('row_linkage')
 
    #instantiate the Cluster object
    c = inchlib_clust.Cluster()
    # read csv data file with specified delimiter, also specify whether there is a header row, the type of the data (numeric/binary) and the string representation of missing/unknown values
    c.read_csv(filename=data, delimiter=",", header=True, datatype="numeric")
    # c.read_data(data, header=bool, missing_value=str/False, datatype="numeric/binary") use read_data() for list of lists instead of a data file

    # normalize data to (0,1) scale, but after clustering write the original data to the heatmap
    c.normalize_data(feature_range=(0,1), write_original=True)

    # cluster data according to the parameters
    c.cluster_data(row_distance=row_distance, row_linkage=row_linkage, axis="both", column_distance="euclidean", column_linkage="ward")

    # instantiate the Dendrogram class with the Cluster instance as an input
    d = inchlib_clust.Dendrogram(c)

    # create the cluster heatmap representation and define whether you want to compress the data by defining the maximum number of heatmap rows, the resulted value of compressed (merged) rows and whether you want to write the features
    d.create_cluster_heatmap(compress=500, compressed_value="median", write_data=True)

    # read metadata file with specified delimiter, also specify whether there is a header row
    # d.add_metadata_from_file(metadata_file="metadata.csv", delimiter=",", header=True, metadata_compressed_value="frequency")

    # read column metadata file with specified delimiter, also specify whether there is a 'header' column
    # d.add_column_metadata_from_file(column_metadata_file="metadata_c.csv", delimiter=",", header=True)
    # export the cluster heatmap on the standard output or to the file if filename specified
    return d.export_cluster_heatmap_as_json()
