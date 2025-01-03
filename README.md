# Efficient Hybrid Classical-Quantum Methods for Protein Ground State Energy Computation via Fragmentation and Reassembly
This repository is made as supporting material for the paper "Efficient Hybrid Classical-Quantum Methods for Protein Ground State Energy Computation via Fragmentation and Reassembly".

### Abstract
Protein characterization is one of the key components for understanding the human body and advancing drug discovery processes. While the future of quantum hardware holds the potential to accurately characterize these molecules, current efforts focus on developing strategies to fragment large molecules into computationally manageable subsystems. In this work, we propose a novel strategy to enable quantum simulation using existing quantum algorithms. Our approach involves fragmenting proteins into their corresponding amino acids, simulating them independently, and then reassembling them post-simulation while applying chemical corrections. This methodology demonstrates its accuracy by calculating the ground state of seven small peptides through reassembling, achieving a relative error of only 0.01 ± 0.02%. Future directions include investigating, with larger quantum computers, whether this approach remains valid for larger proteins.

### Structure of the Repository

There are two folders in this repository:
- Data: corresponds to a dataset composed of the 20 essential amino acids, their corresponding ground state energies and some other common characteristics given by PubChem.
- Code: there are two codes available. One corresponding to the notebook computing the ground state energy of the entire molecules, considered as the ground truth for the experiments. And another code consisting on the computation of the energies through reassembly. For each of the peptides, we analyze their composition in terms of amino acids, and we compute the ground state energy by adding the energies of each amino acid and adding chemical corrections corresponding to the bonding proces. We also provide with the code for the computation of the mean percentage relative error to assess the performance of the strategy.

### How to use it
Depending on your objective, there are two ways of using this repository:
- Run the notebooks to obtain the results presented in the paper.
- If you wish to obtain the energy for another peptide, you can either do it with the reassembling code by changing the sequence of the amino acids. or in the ground truth code by changing the atomic coordinates. We usually obtain the 3D coordinates directly from the PubChem database. 

### Citation
