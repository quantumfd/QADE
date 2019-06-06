#!/usr/bin/python
# -*- coding : utf -8 -*-

import neal
solver = neal.SimulatedAnnealingSampler()
response = solver.sample_ising({'a': -0.5, 'b': 1.0}, {('a', 'b'): -1}, num_reads=2)
response.data_vectors['energy']
toPrint = response.data_vectors['energy']
print(toPrint)