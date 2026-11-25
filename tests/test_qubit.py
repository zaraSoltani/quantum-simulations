import numpy as np
from src.qubit import qubit_state



def test_qubit_normalization():
    psi = qubit_state(3,4j)
    
    norm = np.linalg.norm(psi)
    
    assert np.isclose(norm, 1.0)
