import numpy as np

def compute_protein_energy():
    protein_sequence = input("Enter the protein sequence (e.g., ser-gly-thr): ").lower()
    num_water_molecules = int(input("Enter the number of water molecules lost in bond formation: "))
    
    additional_energies = input("Additional energy corrections in Ha (if lost positive and if added negative): ")
    additional_energies = float(additional_energies) if additional_energies else 0.0
    
    gt = input("Enter the ground truth energy of your protein in Hartrees (if you don't have it leave it blank): ")
    gt = float(gt) if gt else None

    amino_acid_energies = {
        "his": -538.52442,
        "leu": -433.42225,
        "ile": -432.82708,
        "lys": -487.7406,
        "met": -788.02138,
        "phe": -544.43743,
        "thr": -430.09637,
        "trp": -673.57377,
        "val": -394.84749,
        "arg": -595.17254,
        "cys": -710.8573,
        "gln": -521.82178,
        "asn": -519.42952,
        "tyr": -618.27595,
        "ser": -391.51594,
        "gly": -279.11151,
        "asp": -502.76713,
        "glu": -541.3498,
        "pro": -393.7002,
        "ala": -317.69135
    }

    water_energy = -74.9659
    amino_acids = protein_sequence.split('-')

    total_energy = sum(amino_acid_energies.get(aa, 0) for aa in amino_acids)

    total_energy -= num_water_molecules * water_energy

    total_energy += additional_energies
    
    print(f"The final computed energy of {protein_sequence} is: {total_energy:.5f} units")

    if gt is not None:
        dif = np.abs(gt - total_energy)
        error = dif / np.abs(gt)
        percentage_error = error * 100
        print(f"The error of reassembly of {protein_sequence} is of {percentage_error:.2f}%")
    
    return total_energy
