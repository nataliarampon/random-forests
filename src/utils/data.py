import math as m

# For pandas shape method
COLUMNS = 1
ROWS = 0

"""
Checks if all elements in a data frame column are the same
@input column: the data frame column to be analyzed
@output boolean, whether all elements are equal
"""
def all_equal(column):
    vector = column.to_numpy()
    return (vector[0] == vector).all()

"""
Data binning (discretization) of numerical attributes.
Used to transform continuous attributes into categorical ones.
@input data - data frame containing the data
@input attributes - list of attributes names to be binned
@input N - number of bins
@output data frame with discrete attributes
"""
def data_binning(data, attributes, N):
    for attr in attributes:
        bin_width = (data[attr].max() - data[attr].min()) / N
        min_attr = data[attr].min()
        for i, row in data.iterrows():
            bin_number = m.floor((data.loc[i,attr]-min_attr)/bin_width)
            data.loc[i,attr] = bin_number
    return data