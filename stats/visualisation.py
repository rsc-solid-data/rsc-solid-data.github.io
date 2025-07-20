
import numpy as np
import matplotlib.pyplot as plt


def show(atoms: np.ndarray) -> None:
    """
    Enables the visiualisation of the water molecule

    :param atoms: x/y positions of the atoms as an 3x2 NumPy array.
    """
    marks = [r'O', r'H', r'H']
    plt.figure(figsize=(5, 5))
    for i, atom in enumerate(atoms):
        plt.text(atom[0], atom[1], marks[i], zorder=10, 
                 va='center', ha='center', color=f'C{i}', size=30)
    reorderx = np.array([atoms[1], atoms[0], atoms[2]])
    plt.plot(reorderx[:, 0], reorderx[:, 1], 'k--')
    plt.yticks([])
    plt.xticks([])
    plt.ylim([-1.5, 1.5])
    plt.xlim([-1.5, 1.5])
    plt.show()