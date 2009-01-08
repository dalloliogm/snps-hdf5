#!/usr/bin/env python
"""
HDF5 schema for the HGDP snp data

"""

from tables import IsDescription
from tables import Int32Col
from tables import *
import tables
import logging

class Genotype(IsDescription):
    """
    A genotype identified by a snp ID and a individual ID
    """
    snp = StringCol(16)
    individual_id = StringCol(16)
    
    def __init__(self, snp, individual):
        row = self.row
        row['snp'] = str(snp)
        row['individual'] = individual
    
    
    
def create_test_file():
    """
    Create test file and tables
    """
    h5dfile = tables.openFile('../../data/test.h5', mode = 'w', title = 'Test file')
    group = h5dfile.createGroup('/', 'tests', 'Test table')
    
    genotypes_table = h5dfile.createTable(group, 'genotypes', Genotype, 'Genotypes table')
    


def test_all():
    """
    test the current module
    """
    create_test_file()
    import doctest
    doctest.testmod()
        
if __name__ == '__main__':
    test_all()