import networkx as nx 
w5 = nx.wheel_graph(5)

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler = EmbeddingComposite(DWaveSampler())

import dwave_networkx as dnx
print(dnx.min_vertex_cover(w5, sampler))

print(dnx.min_vertex_cover(w5, sampler))