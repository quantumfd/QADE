#!/usr/bin/python
# -*- coding : utf -8 -*-
# 

import dimod
from hybrid.samplers import (
    QPUSubproblemAutoEmbeddingSampler, InterruptableTabuSampler)
from hybrid.decomposers import EnergyImpactDecomposer
from hybrid.composers import SplatComposer
from hybrid.core import State
from hybrid.flow import RacingBranches, ArgMin, Loop
from hybrid.utils import min_sample

# Construct a problem
bqm = dimod.BinaryQuadraticModel({}, {'ab': 1, 'bc': -1, 'ca': 1}, 0, dimod.SPIN)

# Define the solver
iteration = RacingBranches(
    InterruptableTabuSampler(),
    EnergyImpactDecomposer(max_size=2)
    | QPUSubproblemAutoEmbeddingSampler()
    | SplatComposer()
) | ArgMin()
main = Loop(iteration, max_iter=10, convergence=3)

# Solve the problem
init_state = State.from_sample(min_sample(bqm), bqm)
solution = main.run(init_state).result()

# Print results
print("Solution: sample={s.samples.first}".format(s=solution))