#!/Usr/bin/env python
"""

"""

import tables
from schema import Genotype

hdf5_file_path = '../../test.h5'

def create_hdf5_file(test = True):
    """
    Create test file and tables
    
    If test = True, a 
    """
    hdf5file = tables.openFile(hdf5_file_path, mode = 'w', 
                              title = 'genotypes file')
    group = hdf5file.createGroup('/', 'genotypes', 'Genotypes')
    
    hgdp_table = hdf5file.createTable(group, 'genotypes', 
                                          Genotype, 'HGDP genotypes')
    return hdf5file, hgdp_table

def test_file():
    return create_hdf5_file(test = True)
    
def hdf5_file():
    return create_hdf5_file(hdf5_file_path)