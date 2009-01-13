#!/Usr/bin/env python
"""

"""

import tables

h5df_file_path = '../../test.h5'

def create_h5df_file(path = '../../data/test.h5'):
    """
    Create test file and tables
    """
    h5dfile = tables.openFile(path, mode = 'w', 
                              title = 'Testfile')
    group = h5dfile.createGroup('/', 'tests', 'Test table')
    
    genotypes_table = h5dfile.createTable(group, 'genotypes', 
                                          Genotype, 'Genotypes table')
    return h5dfile, group, genotypes_table