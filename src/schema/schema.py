#!/usr/bin/env python
"""
HDF5 schema for the HGDP snp data

"""

from tables import IsDescription
from tables import Int32Col
from tables import *

class Genotype(IsDescription):
    """
    A genotype identified by a snp ID and a individual ID
    """
    snp = StringCol(16)
    

def test_all():
    import doctest
    doctest.testmod()
        
if __name__ == '__main__':
    pass