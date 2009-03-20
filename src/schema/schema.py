#!/usr/bin/env python
"""
HDF5 schema for the HGDP snp data

"""

from tables import *
from numpy import *
import tables
import logging

class SNP(IsDescription):
    """
    A SNP table, containing many nested tables (genotypes, stats)

#    >>> import random; random.seed(0)

#    >>> snp = h5testfile.root.HGDP.snps
#    >>> for i in range(10):
#    >>>     snp['id'] = id
#    >>>     snp['position'] = random.choice(range(1000))
#    >>>     snp['chromosome'] = random.choice(22)

    """

    id = StringCol(20)
    position = UInt16Col()
    chromosome = UInt8Col()

    class genotypes(IsDescription):
        """
        A nested table containing the genotypes of the current snp.
        """
        individual = StringCol(16)
        genotype = EnumCol(('1', '2', '0', '9'), '9', base='uint8')

    class stats(IsDescription):
        """
        A nested table containing some statistics related to the current snp.
        """

        class iHS_by_population(IsDescription):
            """
            A nested table containing iHS by population for the current snp.
            """
            population = StringCol(20)
            iHS = Float64Col()

        class iHS_by_continent(IsDescription):
            """
            A nested table containing iHS by continent for the current snp.
            """
            continent = StringCol(20)
            iHS = Float64Col()

class Individual(IsDescription):
    """
    """

    id = StringCol(20)
    population = StringCol(50)      # Here it will be good to have relationships

    class haplotypes(IsDescription):    # Redundancy!! 
        snp = StringCol(20)
        haplotype1 = EnumCol(('A', 'C', 'G', 'T', '-'), '-', base='uint8')
        haplotype1 = EnumCol(('A', 'C', 'G', 'T', '-'), '-', base='uint8')

def create_testfile():
    """
    Create test file and tables
    """
    h5file = tables.openFile('../data/test.h5', mode = 'w', 
                              title = 'Testfile')
    h5file.createGroup('/', 'tests', 'Tests')
    group = h5file.createGroup('/tests/', 'hgdp', 'hgdp tests')
    
    genotypes_table = h5file.createTable(group, 'snps', 
                                          SNP, 'Genotypes table')
    return h5file, group, genotypes_table


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
