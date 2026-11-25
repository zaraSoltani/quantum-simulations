import numpy as np



def qubit_state(alpha: complex, beta: complex) -> np.ndarray:
    """Construct a normalized single-qubit state."""
    
    
    psi = np.array([alpha, beta], dtype=complex)
    norm = np.linalg.norm(psi)
    
    if norm == 0:
        raise ValueError("The zero vector cannot be normalized.")
    
    return psi / norm




psi = qubit_state(3,4j)
print(psi)

probabilities = np.abs(psi)**2
print(probabilities)

