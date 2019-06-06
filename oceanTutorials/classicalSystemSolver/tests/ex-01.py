#!/usr/bin/python
# -*- coding : utf -8 -*-

import dimod
solver = dimod.ExactSolver()
response = solver.sample_ising({'a': -0.5, 'b': 1.0}, {('a', 'b'): -1})
toPrint = response.data_vectors['energy']
print(toPrint)
