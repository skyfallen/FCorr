'''
FCorr: Basic KD-tree implementation

Copyright 2014, Dmytro Fishman, Konstantin Tretyakov
Licensed under MIT.
'''
import random
import numpy as np

class KDTree:
  '''
  Basic implementation of a random non-incremental KD-tree.
  Note: the standard random module is used for random number generation (i.e. setting random.seed(..) will get you reproducible trees).
  
  Args:
    data (array): A two-dimensional array, with vectors to be indexed in the rows.
    limit (int): Maximal size of a leaf.
    
  >>> random.seed(1)
  >>> data = [10, 40, 20, 30]
  >>> t = KDTree(data)
  >>> t.root.pprint()
  - [@0<>25.000000]
    - [@0<>15.000000]
      - [#0]
      - [#2]
    - [@0<>35.000000]
      - [#3]
      - [#1]
  >>> t.root.size()
  4
  >>> t = KDTree(data, 2)
  >>> t.root.pprint()
  - [@0<>25.000000]
    - [#0,#2]
    - [#1,#3]
  >>> t.find_node(41).pprint()
  - [#1,#3]
  '''
  
  def __init__(self, data, limit=1):
    '''
    Creates the tree.
    
    Args:
      data (array): Numpy array with vectors as rows (or a list).
      limit (int):  Maximum size of a leaf node (if possible).
    '''
    data = np.asarray(data)
    if data.ndim == 1:
      data = data[:, np.newaxis]
    self.root = KDTreeNode(data, range(len(data)), limit)    
  
  def find_node(self, x):
    '''
    Finds the node matching the given element.
    '''
    x = np.asarray(x)
    if x.ndim == 0:
      x = x[np.newaxis]
    return self.root.find(x)

  def find_approximate_nearest_neigbor(self, x):
    '''
    Finds the index of the datapoint which might be the nearest neighbor to x according to the tree.
    '''
    nd = self.find_node(x)
    return nd.idxs[0] # TODO: Fix implementation. Make tests too.


class KDTreeNode:
  def __init__(self, data, idxs, limit):
    '''
    Builds a KD-subtree on a given subset of data recursively. 
    
    Args:
     data (array): a 2d numpy array
     idxs (array of ints): array indices of the data points for which the subtree is created
     limit (int): maximum size of a leaf node, if possible
    '''
    self.idxs = None
    self.left = None
    self.right = None
    self.split_value = None
    self.split_dimension = None
    if len(idxs) <= limit:
      self.idxs = idxs
    else:
      safe = 5
      while safe > 0 and self.left is None:
        safe -= 1
        d = random.randint(0, data.shape[1]-1)
        v = np.median(data[idxs, d])
        left_idxs = [i for i in idxs if data[i, d] < v]
        right_idxs = [i for i in idxs if data[i, d] >= v]
        if len(left_idxs) != 0 and len(right_idxs) != 0:
          self.left = KDTreeNode(data, left_idxs, limit)
          self.right = KDTreeNode(data, right_idxs, limit)
          self.split_dimension = d
          self.split_value = v
      if self.left is None:
        # Can't split to smaller parts, stop building the tree here
        self.idxs = idxs

  def find(self, x):
    '''Queries the tree for a node containing the given point. x must be a 1-d numpy array.'''
    if self.split_dimension is None:
      return self
    else:
      return self.left.find(x) if x[self.split_dimension] < self.split_value else self.right.find(x)
      
  def size(self):
    '''Recursively computes the size of this subtree'''
    if self.idxs is None:
      return self.left.size() + self.right.size()
    else:
      return len(self.idxs)
      
  def pprint(self, indent=0):
    if self.split_dimension is None:
      print '  '*indent + '- [' + ','.join(['#%d' % i for i in self.idxs]) + ']'
    else:
      print '  '*indent + '- [@%d<>%f]' % (self.split_dimension, self.split_value)
      self.left.pprint(indent+1)
      self.right.pprint(indent+1)