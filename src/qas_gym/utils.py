from typing import Dict, List, Optional, Union

import cirq
import numpy as np


def get_default_gates(
        qubits: List[cirq.LineQubit]) -> List[cirq.GateOperation]:
    gates = []
    for idx, qubit in enumerate(qubits):
        next_qubit = qubits[(idx + 1) % len(qubits)]
        gates += [
            cirq.rz(np.pi / 4.)(qubit),
            cirq.X(qubit),
            cirq.Y(qubit),
            cirq.Z(qubit),
            cirq.H(qubit),
            cirq.CNOT(qubit, next_qubit)
        ]
    return gates


def get_default_observables(
        qubits: List[cirq.LineQubit]) -> List[cirq.GateOperation]:
    observables = []
    for qubit in qubits:
        observables += [
            cirq.X(qubit),
            cirq.Y(qubit),
            cirq.Z(qubit),
        ]
    return observables


# def get_bell_state() -> np.ndarray:
#     target = np.zeros(2**2, dtype=complex)
#     target[0] = 1. / np.sqrt(2) + 0.j
#     target[-1] = 1. / np.sqrt(2) + 0.j
#     return target
def get_bell_state() -> np.ndarray:
    final_state = np.zeros((2**2,2**2), dtype=complex)
    state_1 = 1. / np.sqrt(2) + 0.j
    state_2 = -1. / np.sqrt(2) + 0.j
    final_state[0,0] = state_1
    final_state[0,-1] = state_1
    final_state[1,0] = state_1
    final_state[1,-1] = state_2
    final_state[2,1] = state_1
    final_state[2,2] = state_1
    final_state[3,1] = state_1
    final_state[3,2] = state_2
    return final_state


def get_ghz_state(n_qubits: int = 3) -> np.ndarray:
    target = np.zeros(2**n_qubits, dtype=complex)
    target[0] = 1. / np.sqrt(2) + 0.j
    target[-1] = 1. / np.sqrt(2) + 0.j
    return target
