#!/Usr/bin/env python
"""

"""

import tables
from schema import Genotype

hdf5_file_path = '../../test.h5'

def create_hdf5_file(path = '../../data/test.h5'):
    """
    Create test file and tables
    """
    hdf5file = tables.openFile(path, mode = 'w', 
                              title = 'Testfile')
    group = hdf5file.createGroup('/', 'tests', 'Test table')
    
    genotypes_table = hdf5file.createTable(group, 'genotypes', 
                                          Genotype, 'Genotypes table')
    return hdf5file, group, genotypes_table

def test_file():
    create_hdf5_file(path = '../../data/test.h5')
    
def hdf5_file():
    create_hdf5_file()