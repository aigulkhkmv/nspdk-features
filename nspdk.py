import argparse

import networkx as nx
import numpy as np
from eden.graph import Vectorizer
from rdkit import Chem


def rdkmol_to_nx(mol):
    """
    RDKit-mol object to nx.graph
    :param mol: RDKit-mol
    :return: nx.graph
    """
    graph = nx.Graph()
    for e in mol.GetAtoms():
        graph.add_node(e.GetIdx(), label=e.GetSymbol())
    for b in mol.GetBonds():
        graph.add_edge(
            b.GetBeginAtomIdx(), b.GetEndAtomIdx(), label=str(int(b.GetBondTypeAsDouble()))
        )
    return graph


def smiles_strings_to_nx(smiles_list):
    """
    Smiles strings to nx.graph
    :param smiles_list: List[SMILES]
    :return:
    """
    for smiles in smiles_list:
        mol = Chem.MolFromSmiles(smiles)
        yield rdkmol_to_nx(mol)


def load_dataset(input_path):
    """
    Reads txt/smi-file with SMILES\n on a string
    :param input_path: path to file with SMILES
    :return: List[SMILES]
    """
    with open(input_path, "r") as f:
        smiles_list = f.read().strip().split("\n")
    return smiles_list


def smiles2nspdk(input_path, complexity, nbits, save_path):
    """
    Smiles strings to nspdk descriptors
    :param input_path: path to file with SMILES
    :param complexity: descriptor complexity
    :param nbits: bits of descriptor
    :param save_path:
    :return:
    """
    vec = Vectorizer(complexity=complexity, nbits=nbits)
    smiles_list = load_dataset(input_path)
    res = vec.transform(list(smiles_strings_to_nx(smiles_list))).todense()
    output = open(save_path, "w")
    for row in res:
        np.savetxt(output, row)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Path to smi/txt input file")
    parser.add_argument("-o", "--output", help="Path to output file")
    parser.add_argument(
        "-c", "--complexity", help="Complexity of nspdk descriptors. For example 3", type=int
    )
    parser.add_argument("-b", "--nbits", help="Nbits of nspdk descriprors. For example 8", type=int)
    args = parser.parse_args()

    smiles2nspdk(args.input, args.complexity, args.nbits, args.output)
