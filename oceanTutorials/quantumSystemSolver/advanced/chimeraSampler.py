# working with different Topologies
import neal
import dimod
import dwave_networkx as dnx
import networkx as nx 
import dwave.embedding

from dwave.system import DWaveSampler, EmbeddingComposite

# Creating a Chimera Sampler
# 1 - representation of the Chimera graph from graph theory
C16 = dnx.chimera_graph(16)

# 2 - software sampler solver for classical CPU
classical_sampler = neal.SimulatedAnnealingSampler()

# 3 - create a Chimea-Structured sampler
sampler = dimod.StructureComposite(classical_sampler, C16.nodes, C16.edges)

# 4 - the sampler accepts Chimera-structred problem. an Ising problem is created
h = {v: 0.0 for v in C16.nodes}
J = {(u, v): 1 for u, v in C16.edges}
sampleset = sampler.sample_ising(h, J)

# 4' - we can even use the sampler for QPU
embedding_sampler = EmbeddingComposite(sampler)

# 5 - we confirm that teh sampler matches teh DWave struture
qpu_sampler = DWaveSampler(solver={'qpu': True, 'num_active_qubits__within': [2000, 2048]})
QPUGraph = nx.Graph(qpu_sampler.edgelist)
toPrint1 = all(v in C16.nodes for v in QPUGraph.nodes)
print(toPrint1)

toPrint2 = all(edge in C16.edges for edge in QPUGraph.edges)
print(toPrint2)