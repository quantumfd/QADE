import networkx as nx
s5 = nx.star_graph(4)

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler = EmbeddingComposite(DWaveSampler())

import dwave_networkx as dnx 
print(dnx.min_vertex_cover(s5, sampler))