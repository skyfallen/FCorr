'''
FCorr: Math utility functions

Copyright 2014, Dmytro Fishman, Konstantin Tretyakov
Licensed under MIT.
'''
import numpy as np

def standardize(x, axis=0, fix_nan=True):
    """
    Return x minus its mean divided by the standard deviation along the specified axis.
    
    Args:
      x (array): data to be processed, an array or a list will do.
      axis (int): axis=0 means each column is standardized. 
                  axis=1 means each row is standardized.
                  axis=None means global standartization.
      fix_nan (bool): when True, no standardization is done for those cases where stdev = 0.
                      (after mean subtraction the corresponding vectors will become 0)
                      when False, the corresponding vectors will be filled with nan's. 
                      
    Code is inspired by pylab.demean from matplotlib, licensed under PSF which is MIT-compatible.
     
    >>> a = np.array([[1,2,-3],[0,-2,2]])
    >>> standardize(a)
    array([[ 1.,  1., -1.],
           [-1., -1.,  1.]])
    >>> standardize(a, 1)
    array([[ 0.46291005,  0.925... , -1.388...],
           [ 0.        , -1.224...,  1.224...]])
    >>> standardize(a, None)
    array([[ 0.522...,  1.044..., -1.566... ],
           [ 0.        , -1.044...,  1.044...]])
    >>> standardize(1)
    Traceback (most recent call last):
    ...
    ValueError: 0-dimensional data cannot be standardized
    >>> standardize([1])
    array([ 0.])
    >>> standardize([1], fix_nan=False)
    array([ nan])
    >>> standardize([[1, 2], [1, 3]], fix_nan=False)
    array([[ nan,  -1.],
           [ nan,   1.]])
    """
    x = np.asarray(x)
    if x.ndim == 0:
      raise ValueError('0-dimensional data cannot be standardized')
    if axis is None or x.ndim <= 1:
        s = x.std(axis)  # Will be a single number
        if fix_nan and s == 0:
          s = 1
        return (x - x.mean(axis)) / s
    else:
      ind = [slice(None)] * x.ndim
      ind[axis] = np.newaxis
      s = x.std(axis)
      if fix_nan:
        s[s == 0] = 1
      return (x - x.mean(axis)[ind]) / s[ind]
