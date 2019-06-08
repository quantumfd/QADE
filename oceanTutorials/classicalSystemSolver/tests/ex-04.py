import dwavebinarycsp
import dimod 

csp = dwavebinarycsp.factories.random_2in4sat(8,4 ) # 8 variables, 4 clauses

bqm = dwavebinarycsp.stitch(csp)

resp = dimod.ExactSolver().sample(bqm)

for sample, energy in resp.data(['sample', 'energy']):
    print(sample, csp.check(sample), energy)
