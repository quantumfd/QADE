# Quantum interdisciplinary simulation
## Q-iSim

### Quantum Library for Hypersonic Flows

This library is developed to address computational challenges associated with hypersonic flow regimes. The core implementation is written in Rust, with close interoperability with Python for auxiliary components.

The primary numerical solver is implemented in Rust to ensure high performance and memory safety. For modeling chemical reaction processes, an open-source Python library is integrated into the workflow. In particular, the reactive chemistry module leverages PennyLane.

A central solver framework is developed to coordinate and couple multiple sub-solvers, enabling a modular and extensible architecture.

The pre-processing stage, including mesh generation, is performed using Gmsh. Post-processing and visualization of simulation results are carried out using ParaView, along with other open-source tools.

The main focus of this study is to propose a quantum-hybrid software/algorithm, under the GNU license of QuantumFD research project. It has the purpose to provide a viable solution for the problem statement n°2, launched in February 2019 by Airbus Quantum Computing Challenge #qcchallenge (Twitter or LinkedIn), i.e Computatinal Fluid Dyanamics (CFD) on Quantum Computers. 
