#! /usr/bin/env python
"""
Read the SNP file and upload the data to the h5df file
"""

from schema.config import *
import re


def genotypes_parser(handle, ):
    """
    Parse a genotypes file handler.
    
    It returns a Marker object for every line of the file

    >>> from schema.debug_database import *
    >>> print metadata
    MetaData(Engine(sqlite:///:memory:))
    >>> from StringIO import StringIO
    >>> genotypes_file = StringIO(
    ... '''  HGDP00001    HGDP00002    HGDP00003    HGDP00004    HGDP00005    HGDP00006    HGDP00007    HGDP00008    HGDP00009    HGDP000010
    ... rs1112390    AA    GG    AG    AA    AA    AA    AA    AA    AA    AA   
    ... rs1112391    TT    TC    CC    CC    CC    CC    CC    CC    CC    CC
    ... MitoA11252G    AA    AA    AA    AA    AA    AA    AA    AA    AA    AA
    ... rs11124185    TC    TT    TT    TT    TT    TT    TT    TT    TT    TT
    ... MitoA13265G    AA    AA    AA    AA    AA    AA    AA    AA    AA    AA
    ... MitoA13264G    GG    AA    AA    AA    GG    AG    AA    AA    AA    AA
    ... MitoA13781G    AA    AA    AA    AA    AA    AA    --    AA    AA    AA
    ... MitoA14234G    AA    AA    AA    AA    AA    AA    AA    AA    AA    AA
    ... MitoA14583G    AA    AA    AA    AA    AA    AA    AA    AA    AA    AA
    ... MitoA14906G    GG    GG    GG    GG    GG    GG    GG    GG    GG    GG
    ... MitoA15219G    AA    AA    AA    GG    AA    AA    AA    AA    AA    AA''')
    
    >>> snps = genotypes_parser(genotypes_file)
    
    >>> for snp in snps:
    ...     print snp.id, snp.genotypes1, snp.genotypes2
    rs1112390 AGAAAAAAAA AGGAAAAAAA
    rs1112391 TTCCCCCCCC TCCCCCCCCC
    MitoA11252G AAAAAAAAAA AAAAAAAAAA
    rs11124185 TTTTTTTTTT CTTTTTTTTT
    MitoA13265G AAAAAAAAAA AAAAAAAAAA
    MitoA13264G GAAAGAAAAA GAAAGGAAAA
    MitoA13781G AAAAAA-AAA AAAAAA-AAA
    MitoA14234G AAAAAAAAAA AAAAAAAAAA
    MitoA14583G AAAAAAAAAA AAAAAAAAAA
    MitoA14906G GGGGGGGGGG GGGGGGGGGG
    MitoA15219G AAAGAAAAAA AAAGAAAAAA
    """
    # initialize output var
    snps = []
    
    # read the header, containing the Individuals names
#    handle.readline()       # first line is empty??
    header = handle.readline()
    if header is None:
        raise ValueError('Empty file!!')
#    individuals = [Individual(ind_id) for ind_id in header.split()]
    
    # Read snp file line by line.
    for line in handle.readlines():
        fields = line.split()   # TODO: add more rigorous conditions
        if fields is None:
            break
        
        # Initialize a SNP object 
        snp = SNP(id = fields[0])
        snps.append(snp)
        
        # read 
        for n in range(1, len(fields)):
#            current_individual = individuals[n-1]
            current_genotype = fields[n]
            
            snp.genotypes1 += current_genotype[0]
            snp.genotypes2 += current_genotype[1]

    return snps


