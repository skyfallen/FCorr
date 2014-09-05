'''
FCorr: Main module

Copyright 2014, Dmytro Fishman, Konstantin Tretyakov
Licensed under MIT.
'''
import numpy as np

from _math import standardize
from _kdtree import KDTree

class CorrelationIndex:
  '''
    Data structure, that indexes a set of vectors for fast retrieval of 
    elements most correlated with the query point.

    >> fci = CorrelationIndex([(1,3,5), (4,3,2)])
    >> fci.query((1,2,3))
    [0]
    >> fci.query((3,2,1))
    [1]
    >> fci.query((1,2,3), 0)
    []
    >> fci.query((1,2,3), 2)
    [0, 1]
    >> fci.query((3,2,1), 3)
    [1, 0]

    >> fci = CorrelationIndex([])
    >> fci.query((1,2,3))
    []

    >> fci = CorrelationIndex("random string")
    Traceback (most recent call last):
        ...
    ValueError: object is not iterable

    >> fci = CorrelationIndex([(1,3,5), (4,3)])
    Traceback (most recent call last):
        ...
    ValueError: iterable should contain tuples (or vectors or lists) of numbers of equal length
  '''

  def __init__(self, data):
    '''
      Reads the data, standardizes it and creates an index based on the data.

      Args:
         data (array): A two-dimensional array, with vectors to be indexed in the rows. 
            Preferably a numpy array, but other iterables (e.g. list of lists of the same length) could work too.
      Raises:
         ValueError, TypeError or something like that, if the dataset is invalid.
    '''
    standardized_data = standardize(data)
    self._tree = KDTree(standardized_data) # Index the data

  def query(self, x, matches=1):
    #TODO: Implement
    return [self._tree.find_approximate_nearest_neigbor(x)]
    