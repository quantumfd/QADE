import dwavebinarycsp

def logic_circuit(a, b, c, d, z):
    not1 = not b 
    or2 = b or c 
    and3 = a and not1 
    or4 = or2 or d 
    and5 = and3 and or4 
    not6 = not or4 
    or7 = and5 or not6 
    return (z == or7)

csp = dwavebinarycsp.ConstraintSatisfactionProblem(dwavebinarycsp.BINARY)
csp.add_constraint(logic_circuit, ['a', 'b', 'c', 'd', 'z'])

# Convert the binary constraint satisfaction problem to a binary quadratic model
bqm = dwavebinarycsp.stitch(csp)

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

sampler = EmbeddingComposite(DWaveSampler())

# sampling pool 10 samples
response = sampler.sample(bqm, num_reads=10)

# Check how many solutions meet the constraints (are valid)
valid, invalid, data = 0, 0, []
for datum in response.data(['sample', 'energy', 'num_occurrences']):
    if (csp.check(datum.sample)):
        valid = valid+datum.num_occurrences
        for i in range(datum.num_occurrences):
            data.append((datum.sample, datum.energy, '1'))
    else:
        invalid = invalid+datum.num_occurrences
        for i in range(datum.num_occurrences):
            data.append((datum.sample, datum.energy, '0'))
print(valid, invalid)

print(next(response.samples()))