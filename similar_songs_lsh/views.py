"""Flask view functions: upload page and song similarity analysis."""

from flask import render_template, request
import pandas as pd

from similar_songs_lsh.features import extract_mfcc
from similar_songs_lsh.lsh import find_nearest_neighbors

def index():
    return render_template('index.html')

def analyse():
    file_path = request.form['file_path']
    # Do something with file_path
    df = pd.read_csv("C:\\Users\\Farhan\\Desktop\\pycharm projects\\mfcc_feature.csv")
    arr1 = df.values

    mfcc_new = extract_mfcc(file_path)
    query_result = find_nearest_neighbors(df,mfcc_new)  # , num_permutations=100, band_width=5, num_neighbors=5)#, jaccard_threshold=0.5)

    # Print the result
    output = str()
    if not query_result:
        output = "No match found"
    else:
        output = "Approximate nearest neighbors with Jaccard similarity >0.5:" + str(query_result)
    return render_template('play.html', file_path=output)
