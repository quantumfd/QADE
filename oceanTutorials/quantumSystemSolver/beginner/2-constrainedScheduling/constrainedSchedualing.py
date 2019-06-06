def scheduling(time, location, lenght, mandatory):
    if time:                                    # Business hours
        return (location and mandatory)         # In office and mandatory
    else:                                       # Outside business hours
        return((not location) and lenght)       # Teleconference for a short duration

import dwavebinarycsp
csp = dwavebinarycsp.ConstraintSatisfactionProblem(dwavebinarycsp.BINARY)
csp.add_constraint(scheduling, ['time', 'location', 'length', 'mandatory'])

bqm = dwavebinarycsp.stitch(csp)
bqm.linear
{'length': -2.0, 'location': 2.0, 'mandatory': 0.0, 'time': 2.0}
bqm.quadratic
{('location', 'length'): 2.0,
 ('mandatory', 'length'): 0.0,
 ('mandatory', 'location'): -2.0,
 ('time', 'length'): 0.0,
 ('time', 'location'): -4.0,
 ('time', 'mandatory'): 0.0}

### Quantum QPU - D-Wave
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler = EmbeddingComposite(DWaveSampler())

response = sampler.sample(bqm, num_reads=100)
total = 0

min_energy = next(response.data(['energy']))[0]
print(min_energy)

for sample, energy, occurrences in response.data(['sample', 'energy', 'num_occurrences']):
    total = total + occurrences
    if energy == min_energy:
        time = 'business hours' if sample['time'] else 'evenings'
        location = 'office' if sample['location'] else 'home'
        length = 'short' if sample['length'] else 'long'
        mandatory = 'mandatory' if sample['mandatory'] else 'optional'
        print("{}: During {} at {}, you can schedule a {} meeting that is {}".format(occurrences, time, location, length, mandatory))
print("Total occurences: ", total)