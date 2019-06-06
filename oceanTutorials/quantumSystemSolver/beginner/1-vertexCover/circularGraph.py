import networkx as nx 
c5 = nx.circular_ladder_graph(5)

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler = EmbeddingComposite(DWaveSampler())

import dwave_networkx as dnx 
print(dnx.min_vertex_cover(c5, sampler))

print(dnx.min_vertex_cover(c5, sampler))