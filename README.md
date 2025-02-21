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
self.Q = np.diag([2.0, 5.0, 15.0, 8.0])  # State cost
self.R = np.array([[0.10]])  # Control cost
```

**Results**: Due to inadequate tuning, the system fails to maintain stability, and the pendulum falls after 15 seconds.

**Recording**: View Configuration 1 Performance

#### Configuration 2 (Optimized):
```python
self.Q = np.diag([1.0, 4.5, 17.0, 8.5])  # State cost
self.R = np.array([[0.06]])  # Control cost
```

**Results**: The controller effectively stabilizes the pendulum, allowing it to remain upright despite the earthquake disturbances.

**Recording**: View Configuration 2 Performance

## Setup & Installation

### Prerequisites

- **ROS2 Jazzy**
- **Gazebo Garden**
- **Python 3.8+**
- **Required Packages**: numpy, scipy, control

### Installation Commands

```bash
# Set ROS_DISTRO as per your configuration
export ROS_DISTRO=jazzy

# Install ROS2 packages
sudo apt update
sudo apt install -y \
    ros-$ROS_DISTRO-ros-gz-bridge \
    ros-$ROS_DISTRO-ros-gz-sim \
    ros-$ROS_DISTRO-ros-gz-interfaces \
    ros-$ROS_DISTRO-robot-state-publisher \
    ros-$ROS_DISTRO-rviz2

# Install Python dependencies
pip3 install numpy scipy control
```

### Repository Setup

```bash
# Clone your fork
cd ~/
git clone https://github.com/YOUR_USERNAME/RAS-SES-598-Space-Robotics-and-AI.git

# Navigate to your ROS2 workspace
cd ~/ros2_ws/src
ln -s ~/RAS-SES-598-Space-Robotics-and-AI/assignments/cart_pole_optimal_control .

# Build the package
cd ~/ros2_ws
colcon build --packages-select cart_pole_optimal_control --symlink-install

# Source the workspace
source install/setup.bash
```

### Running the Simulation

```bash
ros2 launch cart_pole_optimal_control cart_pole_rviz.launch.py
```

This will start:

- Gazebo simulation
- RViz visualization
- LQR controller
- Earthquake force generator
- Force visualizer

## Performance Analysis

### Metrics Evaluated

- Maximum Pole Angle Deviation
- RMS Cart Position Error
- Peak Control Force Used
- Recovery Time After Disturbances

### Observations

- The optimized LQR configuration demonstrates better stability and lower control effort, successfully handling seismic disturbances.

## Future Enhancements

- Implement reinforcement learning (DQN) for adaptive control
- Explore additional control strategies such as MPC
- Optimize earthquake force rejection through disturbance observers

## License

This project is part of the RAS-SES-598 Space Robotics and AI course.

