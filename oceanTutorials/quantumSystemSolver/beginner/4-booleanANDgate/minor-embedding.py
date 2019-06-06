from dwave.system.samplers import DWaveSampler
from dwave.system.composites import FixedEmbeddingComposite

embedding = {'x1': {1}, 'x2': {5}, 'z': {0, 4}}
sampler = DWaveSampler()
sampler_embedded = FixedEmbeddingComposite(sampler, embedding)
print(sampler_embedded.adjacency)

Q = {('x1', 'x2'): 1, ('x1', 'z'): -2, ('x2', 'z'): -2, ('z', 'z'): 3}
response = sampler_embedded.sample_qubo(Q, num_reads=100)
for datum in response.data(['sample', 'energy', 'num_occurrences']):
    print(datum.sample, "Energy: ", datum.energy, "Occurrences: ", datum.num_occurrences)