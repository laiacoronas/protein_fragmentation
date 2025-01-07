# Efficient Protein Ground State Energy Computation via Fragmentation and Reassembly
This repository is made as supporting material for the paper "Efficient Protein Ground State Energy Computation via Fragmentation and Reassembly".

### Abstract
Protein characterization is one of the key components for understanding the human body and advancing drug discovery processes. While the future of quantum hardware holds the potential to accurately characterize these molecules, current efforts focus on developing strategies to fragment large molecules into computationally manageable subsystems. In this work, we propose a novel strategy to enable quantum simulation using existing quantum algorithms. Our approach involves fragmenting proteins into their corresponding amino acids, simulating them independently, and then reassembling them post-simulation while applying chemical corrections. This methodology demonstrates its accuracy by calculating the ground state of seven small peptides through reassembling, achieving a relative error of only  0.00263 ± 0.01724%. Future directions include investigating, with larger quantum computers, whether this approach remains valid for larger proteins.

### Structure of the Repository

There are two folders in this repository:
- Data: corresponds to a dataset composed of the 20 essential amino acids, their corresponding ground state energies and some other common characteristics given by PubChem.
- Codes: there are three codes available. "ground_truth" corresponds to the notebook computing classically the ground state energy of the entire peptides, considered as the ground truth for the experiments. A second named "energy_computation" that accounds for an automated pipeline to input your own proteins and get their corresponding energy. And the last one name "reassembly" that accounts for a detailed tutorial on how we fragment and reassembly the peptides to get the final energies. There we also explain how to use the "energy_computation" code to get your own energies.

### How to use it
Depending on your objective, there are two ways of using this repository:
- Run the codes to obtain the results presented in the paper.
- If you wish to obtain the energy for another peptide, you can either do it with the reassembling code by inputing you amino acid sequence or in the ground truth code by changing the atomic coordinates. We usually obtain the 3D coordinates directly from the PubChem database. 

### Citation
