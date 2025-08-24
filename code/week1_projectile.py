# Week 1: Projectile Motion Simulation (Classical Physics Warmup)
# Author: Jenkem
# Purpose: Simulate the motion of a projectile under gravity.

import numpy as np
import matplotlib.pyplot as plt

# --- PARAMETERS ---
v0 = 20       # initial speed in m/s
angle = 45    # launch angle in degrees
g = 9.8       # acceleration due to gravity (m/s^2)

# --- CALCULATIONS ---
theta = np.radians(angle)         # convert angle to radians
v0x = v0 * np.cos(theta)          # x-component of velocity
v0y = v0 * np.sin(theta)          # y-component of velocity

t_flight = 2 * v0y / g            # total time of flight
t = np.linspace(0, t_flight, 100) # time steps

# positions
x = v0x * t
y = v0y * t - 0.5 * g * t**2

# --- PLOTTING ---
plt.figure(figsize=(8,5))
plt.plot(x, y, label="Projectile path")
plt.title("Projectile Motion (Week 1)")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Height (m)")
plt.grid(True)
plt.legend()
plt.show()
