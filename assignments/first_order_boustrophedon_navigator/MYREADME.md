Final Parameter Values with Justification

Controller Gains:
Linear Velocity Control:
Kp (Proportional Gain): 15.0

Kd (Derivative Gain): 1.05

Angular Velocity Control:
Kp (Proportional Gain): 12.0

Kd (Derivative Gain): 0.05

Justification:

Kp was increased step by step until the system responded quickly without becoming unstable.
Kd was fine-tuned to reduce oscillations and overshooting caused by high Kp values.
These gains were chosen based on iterative tests, balancing performance and stability.
Performance Metrics and Analysis

Final Cross-Track Error: ~0.025 meters .
Steady-State Velocity: ~2.5 m/s.
Overshoot: Less than 5% for both linear and angular control.
System Stability: Maintains stability in straight paths and sharp turns.
Analysis:
The system achieved accurate trajectory tracking and smooth velocity transitions, with minimal overshooting. Both linear and angular controllers worked together to maintain stability and reduce deviations.

Plots

1. Cross-Track Error Over Time
Observation: The cross-track error decreases over time, stabilizing near zero.
2. Trajectory Plot
Blue Line: Desired Path
Red Line: Actual Path
Observation: The actual path closely follows the desired trajectory with minimal deviation.
3. Velocity Profile
Observation: The velocity stabilizes at ~2.5 m/s with smooth changes during acceleration and deceleration.
Discussion of Tuning Methodology

Initial Parameter Guess:
Started with low Kp and Kd values to prevent instability.
Step-by-Step Tuning:
Increased Kp (Linear) to improve response time for velocity control.
Adjusted Kd (Linear) to minimize velocity oscillations and ensure smooth transitions.
Increased Kp (Angular) to achieve precise angular corrections for path following.
Tuned Kd (Angular) to dampen angular oscillations and reduce overshoot.
Testing and Iteration:
Ran tests on straight paths, curves, and sharp turns.
Observed performance metrics (cross-track error, overshoot, and stability) and adjusted gains iteratively.
Challenges and Solutions

Challenge 1: Overshooting with high Kp values.
Solution: Increased Kd to counteract overshoot and stabilize the response.
Challenge 2: Oscillations in angular velocity during sharp turns.
Solution: Tuned Kd (Angular) to dampen oscillations effectively.
Challenge 3: Balancing quick response and stability.
Solution: Iterative tuning of both Kp and Kd for linear and angular controls until optimal performance was achieved.