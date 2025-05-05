
import numpy as np
import matplotlib.pyplot as plt

# Generate angle values from 0 to 2π (360°)
theta = np.linspace(0, 2 * np.pi, 1000)

# Radiation pattern for a simple dipole antenna: |cos(θ)|
r = np.abs(np.cos(theta))

# Create a polar plot
plt.figure()
plt.polar(theta, r)
plt.title("Dipole Antenna Radiation Pattern")
plt.show()
