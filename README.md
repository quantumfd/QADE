QADE
Quantum Algorithm Development - Research Project

oceanTutorials - All Copyrights (C) rights belong to D-Wave System Inc.

oceanTutorials - includes all the examples on how to use a D-Wave Quantum Computer device.

erin - All Copyrights (C) belongs to Ovidiu-Ionut Michiu/QuantumFD Project

~ ERIN ~ 
or
~ Enclosed inteRdIsciplinary simulatioNs ~

The main focus of this study is to propose a quantum-hybrid software/algorithm, under the GNU license of QuantumFD research project. It has the purpose to provide a viable solution for the problem statement n°2, launched in February 2019 by Airbus Quantum Computing Challenge #qcchallenge (Twitter or LinkedIn), i.e Computatinal Fluid Dyanamics (CFD) on Quantum Computers. 

The quantum-hybrid algorithm is designed to run on a D-Wave quantum annealing system. The quantum device is located in Canada. The access for the numerical simulation will be made via a cloud connection, provided under Leap Program offered by the canadian partner. The codes written under the GNU license of QuantumFD project, will use the "ocean" software proposed by D-Wave System Inc.

The codes are written using the programming language Python, version 3.7 or above. Additionally, the PIL(Python Imaging Library) is required to open the Python quantum-hybrid code.

Before testing the code, it is adviasible to build a virtual environment where all the dependencies required will be installed. 

Dependencies:
	~ Your PC and connection with D-Wave ~
	+ build a virtual environment
	+ install pip (package installer for python)
	+ install ocean-sdk software provided by D-Wave System Inc.
	+ install Python version 3.6 or above 
	+ install PIL packages
	+ install networkx
	+ install matplotlib - used for graph visualization
	
	~ CFD ~
	+ pre-processing -> install Gmsh or Cassioppee (from ONERA) - both are open-source software
	+ processing -> install SU2 - open-source software 
	+ post-processing -> install ParaView - an open-source software used to visualize the results