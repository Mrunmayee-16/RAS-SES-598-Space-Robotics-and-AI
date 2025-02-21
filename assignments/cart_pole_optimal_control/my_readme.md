# Cart-Pole Optimal Control

## Overview

This project involves tuning and analyzing an LQR (Linear Quadratic Regulator) controller for a cart-pole system subjected to earthquake disturbances. The objective is to maintain the inverted pendulum's stability while ensuring the cart remains within its physical constraints despite external perturbations.

## System Description

The system follows the formalism from the Underactuated Robotics Cart-Pole Problem.

### Physical Setup

- **Cart-Pole System**: An inverted pendulum mounted on a cart
- **Cart Traversal Range**: ±2.5m (Total: 5m)
- **Pole Length**: 1m
- **Cart Mass**: 1.0 kg
- **Pole Mass**: 1.0 kg

### Disturbance Generator

The earthquake force generator introduces external perturbations through:

- Superposition of sine waves
- Base amplitude: 15.0N
- Frequency range: 0.5-4.0 Hz
- Random variations in amplitude and phase
- Additional Gaussian noise

## LQR Tuning & Performance Analysis

### Configurations Tested

#### Configuration 1:
```python
self.Q = np.diag([1.5, 1.5, 15.0, 10.0])  # State cost
self.R = np.array([[0.06]])  # Control cost
```

**Results**: Due to inadequate tuning, the system fails to maintain stability, and the pendulum falls after 15 seconds.

**Recording**: View Configuration 1 Performance

#### Configuration 2 (Optimized):
```python
self.Q = np.diag([1.2, 1.8, 18.0, 10.0])  # State cost
self.R = np.array([[0.06]])  # Control cost
```

**Results**: The controller effectively stabilizes the pendulum, allowing it to remain upright despite the earthquake disturbances.

**Recording**: View Configuration 2 Performance

### Observations

- The optimized LQR configuration demonstrates better stability and lower control effort, successfully handling seismic disturbances.