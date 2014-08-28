'''
FCorr: Main module

Copyright 2014, Dmytro Fishman, Konstantin Tretyakov
Licensed under MIT.
'''
import numpy as np

class CorrelationIndex:
  '''
    Data structure, that indexes a set of vectors for fast retrieval of 
    elements most correlated with the query point.

    >>> fci = CorrelationIndex([(1,3,5), (4,3,2)])
    >>> fci.query((1,2,3))
    [0]
    >>> fci.query((3,2,1))
    [1]
    >>> fci.query((1,2,3), 0)
    []
    >>> fci.query((1,2,3), 2)
    [0, 1]
    >>> fci.query((3,2,1), 3)
    [1, 0]

    >>> fci = CorrelationIndex([])
    >>> fci.query((1,2,3))
    []

    >>> fci = CorrelationIndex("random string")
    Traceback (most recent call last):
        ...
    ValueError: object is not iterable

    >>> fci = CorrelationIndex([(1,3,5), (4,3)])
    Traceback (most recent call last):
        ...
    ValueError: iterable should contain tuples (or vectors or lists) of numbers of equal length
  '''

  def __init__(self, data):
    '''
      Reads the data, standardizes it and creates an index based on the data.

      Args:
         data - the dataset to be indexed.
                It must be given as an iterable, containing tuples (or vectors or lists)
                of numbers of equal length. E.g. [(1,2), (3,4)] is a valid dataset.
      Raises:
         ValueError, if the dataset is invalid.
    '''
    
    # Accepted formats are: numpy.array, list, arrays, tuples    
    if not hasattr(data, '__iter__'):
      raise ValueError("object is not iterable")

    # If input is empty return empty kd-tree
    if not data:
      return None

    if max(data, key = len) != min(data, key = len):
      raise ValueError("iterable should contain tuples (or vectors or lists) of numbers of equal length")

    # Standardization procedure: subtract mean and divide by standard deviation 
    standardized_data = _standardize(data)

    # Index standardized data
    self.left_child = None
    self.right_child = None
    self.median = None
    self = _index(standardized_data, self)
    return self

  def _index(data, tree_node):
    '''
      Recursively constructs K dimensional tree (KD tree) that indexes data. This structure
          will be used to perform an approximate search for the k nearest neighbors.

      Args:
          data - Standardized iterable, containing tuples (or vectors or lists)
                of numbers of equal length.
          tree_node - node of the KD tree. If size(data) > 1, it will store a median value by which 
                data will be divided into two parts and pointers to the left and right subtree,
                else it will store this point index. 
      Returns:
          tree_node - complete node with either median and two pointers (left and right subtrees) or point index
    '''
    #if len(data) == 1:
    #  return 
  
  def _standardize(self, data):
    '''
      Row wise standardization of an input data: for the each row in the input data from each value in the row
                subtracts row mean and divides by row standard deviation

      Args:
         data - the dataset to be standardized.
                It must be given as an iterable, containing tuples (or vectors or lists)
                of numbers of equal length. E.g. [(1,2), (3,4)] is a valid dataset.
      Returns:
          standardized_data - input data where for each value in each row mean of the row was subtracted and divided by the 
                row standard deviation

      >>> CorrelationIndex([])._standardize([1,2,3])
      array([-1.22474487,  0.        ,  1.22474487])

      >>> CorrelationIndex([])._standardize([1,2])
      array([-1.,  1.])

      >>> CorrelationIndex([])._standardize([[1,2,3],[2,3,4]])
      array([[-1.22474487,  0.        ,  1.22474487],
             [-1.22474487,  0.        ,  1.22474487]])

      Warning: crappy code here, 'm not sure if it works for all data types

      Pseudo code:
      if there is an input data was one dimensional vector 
        return standardized_data vector
      else 
        initialize standardized_data with 0s
      for each or the rows in the input data
        from each element subtract mean(row) and divide by std(row)
      return standardized ndim array
    '''
    if isinstance(data[0], int):
      return (data - np.mean(data))/np.std(data)
    else:
      stdandardized_data = np.zeros((len(data), len(data[0])))

    for index in range(len(data)):
      stdandardized_data[index] = (data[index] - np.mean(data[index]))/np.std(data[index])
    return stdandardized_data
  
  def _build_kd_tree(std_data_set):
    '''
    constructs and returns kd-tree for the given data set
    '''
    return
