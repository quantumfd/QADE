Q_not = {('x', 'x'): -1, ('x', 'z'): 2, ('z', 'x'): 0, ('z', 'z'): -1}

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler = DWaveSampler()
sampler_embedded = EmbeddingComposite(sampler)

print(sampler.adjacency[sampler.nodelist[0]])

from dwave.system.composites import FixedEmbeddingComposite
sampler_embedded = FixedEmbeddingComposite(sampler, {'x': [0], 'z': [4]})
print(sampler_embedded.adjacency)

response = sampler_embedded.sample_qubo(Q_not, num_reads=10)
for datum in response.data(['sample', 'energy', 'num_occurrences']):
    print(datum.sample, "Energy: ", datum.energy, "Occurrences: ", datum.num_occurrences)
