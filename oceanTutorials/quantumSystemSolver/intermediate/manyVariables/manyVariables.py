# Represent the graph problem as a binary quadratic model
import dimod 
import networkx as nx 
import random 

#Formulate the problem
graph = nx.barabasi_albert_graph(100, 3, seed=1)    # Build a quasi-random graph
# Set node and edge values for the problem
h = {v: 0.0 for v in graph.nodes}
J = {edge: random.choice([-1, 1]) for edge in graph.edges}
bqm = dimod.BQM(h, J, offset=0, vartype=dimod.SPIN)

# Create a Hybrid Workflow
# Set a workflow of tabu search in parallel to submissions to a D-Wave system
import hybrid 
workflow = hybrid.Loop(
    hybrid.RacingBranches(
        hybrid.InterruptableTabuSampler(),
        hybrid.EnergyImpactDecomposer(size=30, rolling=True, rolling_history=0.75)
        | hybrid.QPUSubproblemAutoEmbeddingSampler()
        | hybrid.SplatComposer()) | hybrid.ArgMin(), convergence=3)

# Solve the Problem using Hybrid Resources
# Convert to dimod sampler and run workflow
result = hybrid.HybridSampler(workflow).sample(bqm)

print("Solution: sample={}".format(result.first))