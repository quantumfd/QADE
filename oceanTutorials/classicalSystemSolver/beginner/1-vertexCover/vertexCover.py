import networkx as nx
s5 = nx.star_graph(4)

from dimod.reference.samplers import ExactSolver
sampler = ExactSolver()

import dwave_networkx as dnx 
print(dnx.min_vertex_cover(s5, sampler))