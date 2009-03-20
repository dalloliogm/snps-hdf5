#!/usr/bin/env python
"""
HDF5 schema for the HGDP snp data

"""

from tables import *
from numpy import *
import tables
import logging

genotypes = tables.Enum(['0', '1', '2', '9'])

class SNP(IsDescription):
    """
    A SNP table, containing many nested tables (genotypes, stats)

    import random; random.seed(0)

    snp = h5testfile.root.HGDP.snps
    for i in range(10):
        snp['id'] = id
        snp['position'] = random.choice(range(1000))
        snp['chromosome'] = random.choice(22)

    """

    id = StringCol(20)
    position = UInt16Col()
    chromosome = UInt8Col()

    class genotypes(IsDescription):
        """
        A genotype identified by a snp ID and a individual ID
        
         
        """
        individual = StringCol(16)
        genotype = EnumCol(genotypes, '9', base='uint8')

    class stats(IsDescription):

        class iHS_by_population(IsDescription):
            population = StringCol(20)
            iHS = Float64Col()

        class iHS_by_continent(IsDescription):
            continent = StringCol(20)
            iHS = Float64Col()


   
def create_testfile():
    """
    Create test file and tables
    """
    h5dfile = tables.openFile('../data/test.h5', mode = 'w', 
                              title = 'Testfile')
    group = h5dfile.createGroup('/', 'tests', 'Test table')
    
    genotypes_table = h5dfile.createTable(group, 'genotypes', 
                                          GenotypeDescriptor, 'Genotypes table')
    return h5dfile, group, genotypes_table


def test_all():
    """
    test the current module
    """
    logging.basicConfig(level=logging.DEBUG)
    create_testfile()
    import doctest
    doctest.testmod()
        
if __name__ == '__main__':
    test_all()
