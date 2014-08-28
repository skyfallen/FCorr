'''
FCorr: Test module.

Meant for use with py.test.
Write each test as a function named test_<something>.
Read more here: http://pytest.org/

Copyright 2014, Dmytro Fishman
Licensed under MIT
'''

def test_example():
    assert True

'''
def test_my_module():    
    # Input - set of vectors / lists / tuples or two-dimensional array
    #    [(1,2,3), (3,4,5), ...]
    #    [[1,2,3], [3,4,5], ...]
    #    numpy.array([[1,2],[3,4]])
    #    ... etc, anything that supports iteration and produces vectors.
    # If data is incorrect (wrong format, different dimensions, etc)
    #     -> raise ValueError("Message")
    # 
    # Non-incremental only Max-Correlation
    # Operations:
    #    1. Indexing data
    #
    #       - .index(data)  [in constructor]
    #
    #    2. Querying the data structure.
    #  
    #       - .query(point, n=1)   -> returns the n nearest points from the dataset.
    #
    #       Versions:
    #          - return list of indices of n nearest neighbors
    #            depending on implementation, those may be sorted according to correlation.
    #
    #     3. [internal, if needed]
    #        - .query_detailed(point, n=1)
    #          -> returns list of (index, correlation value)
    #
    #

    # Sample use case:
    from fcorr import CorrelationIndex
    fci = CorrelationIndex(data)    => For non-incremental index raise exception on empty data
    
    fci.query(point, 0) --> empty list
    fci.query(point, -1) --> ValueError
    fci.query(point, 2) --> two results
    fci.query(point, 1000000000) -> list of length len(data)
    fci.query(point, 'bla') --> error message 'wrong type'
    fci = CorrelationIndex([])
    fci.query(point) --> []

    sample_data = [(10,)]
    fci = CorrelationIndex(sample_data)
    assert fci.query((1,)) == [0]    ==> Must work reasonably with vectors of dimension 1 too



def test_my_module():
    from fcorr import standardize
    import numpy

    sample_data = []
    sample_data = None
    sample_data = [[1],[2],[3]]
    assert standardize(sample_data) == [[-1],[0],[1]]

    sample_data1 = numpy.array([1],[2],[3])
    assert standardize(sample_data) == numpy.array([-1],[0],[1])
'''