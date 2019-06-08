import dwavebinarycsp
import dwavebinarycsp.factories.constraint.gates as gates 
import operator 

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
csp.add_constraint(operator.ne, ['b', 'not1'])  # add NOT 1 gate
csp.add_constraint(gates.or_gate(['b', 'c', 'or2']))    # add OR 2 gate
csp.add_constraint(gates.and_gate(['a', 'not1', 'and3']))   # add AND 3 gate
csp.add_constraint(gates.or_gate(['d', 'or2', 'or4']))  # add OR 4 gate
csp.add_constraint(gates.and_gate(['and3', 'or4', 'and5'])) # add AND 5 gate
csp.add_constraint(operator.ne, ['or4', 'not6'])    # add NOT 6 gate
csp.add_constraint(gates.or_gate(['and5', 'not6', 'z']))    # add OR 7 gate

# Convert the binary constraint satisfaction problem to a binary quadratic model
bqm = dwavebinarycsp.stitch(csp)

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

sampler = EmbeddingComposite(DWaveSampler())

# sampling pool 10 samples
response = sampler.sample(bqm, num_reads=50)

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

import matplotlib.pyplot as plt 
plt.ion()
plt.scatter(range(len(data)), [x[1] for x in data], c=['y' if (x[2] =='1')
            else 'r' for x in data], marker='.')
plt.xlabel('Sample')
plt.ylabel('Energy')
plt.show()

for datum in response.data(['sample', 'energy', 'num_occurrences', 'chain_break_fraction']):
    print(datum)