# working with different topologies
import neal 
import dimod 
import dwave_networkx as dnx 
import networkx as nx 
import dwave.embedding 

from dwave.system import DWaveSampler, EmbeddingComposite

# Creating a Pegasus Sampler
P6 = dnx.pegasus_graph(6)
classical_sampler = neal.SimulatedAnnealingSampler()
sampler = dimod.StructureComposite(classical_sampler, P6.nodes, P6.edges)

# working with embeddings
num_variables = 40
embedding = dwave.embedding.chimera.find_clique_embedding(num_variables, 16)
toPrint1 = max(len(chain) for chain in embedding.values())
print(toPrint1)

num_variables = 40
embedding = dwave.embedding.pegasus.find_clique_embedding(num_variables
, 6)
toPrint2 = max(len(chain) for chain in embedding.values())
print(toPrint2)