# Cart-Pole Optimal Control
[Screencast from 02-20-2025 12_15_23 PM.webm](https://github.com/user-attachments/assets/d63818d4-6a36-4d7f-9fd7-7779781ce95a)

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
self.Q = np.diag([2.0, 5.0, 15.0, 8.0])  # State cost
self.R = np.array([[0.10]])  # Control cost
[Screencast from 02-20-2025 12_15_23 PM.webm](https://github.com/user-attachments/assets/d63818d4-6a36-4d7f-9fd7-7779781ce95a)

**Results**: Due to inadequate tuning, the system fails to maintain stability, and the pendulum falls after 15 seconds.

**Recording**: View Configuration 1 Performance

#### Configuration 2 (Optimized):
```python
self.Q = np.diag([1.0, 4.5, 17.0, 8.5])  # State cost
self.R = np.array([[0.10]])  # Control cost
```
[Screencast from 02-20-2025 12_17_08 PM.webm](https://github.com/user-attachments/assets/cde72b1c-49f1-4fa4-adb6-99dca2ce3684)

**Results**: The controller effectively stabilizes the pendulum, allowing it to remain upright despite the earthquake disturbances.

**Recording**: View Configuration 2 Performance

### Observations

- The optimized LQR configuration demonstrates better stability and lower control effort, successfully handling seismic disturbances.
