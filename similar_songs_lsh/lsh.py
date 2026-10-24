"""Approximate nearest neighbours with a MinHash LSH Forest."""

from datasketch import MinHash, MinHashLSHForest

def find_nearest_neighbors(df_, to_check):  # , jaccard_threshold=0.5):
    # Create an instance of MinHash with the given number of permutations
    num_permutations = 100
    band_width = 10
    num_neighbors = 10
    minhash = MinHash(num_perm=num_permutations)

    lsh = MinHashLSHForest(num_perm=num_permutations, l=band_width)

    # Counter for the index of the data
    counter = 0

    # Loop through the rows of the dataframe and update the MinHash object for each column value
    for i in df_.index:
        # Create a new MinHash object for each row
        minhash = MinHash(num_perm=num_permutations)
        for j in df_.iloc[i]:
            # Update the MinHash object with the string representation of the column value
            minhash.update(str(j).encode('utf8'))
        # Add the MinHash object to the LSH Forest with a unique label
        lsh.add("data point " + str(counter), minhash)
        # Increment the counter
        counter += 1

    # Build the index for the LSH Forest
    lsh.index()

    # Create a new MinHash object for the query data
    query_minhash = MinHash(num_perm=num_permutations)

    # Loop through the query data and update the MinHash object for each value
    query_data = df_.iloc[4]
    #query_data = to_check
    for j in query_data:
        query_minhash.update(str(j).encode("utf8"))

    # Query the LSH Forest for the nearest neighbors to the query MinHash object with Jaccard similarity greater than jaccard_threshold
    query_result_ = lsh.query(query_minhash, num_neighbors)

    # Return the query result
    return query_result_
