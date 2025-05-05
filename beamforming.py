import numpy as np
import matplotlib.pyplot as plt

# Define angle values for plot
theta = np.linspace(-np.pi, np.pi, 1000)

# Parameters for antenna array
N = 8        # number of elements
d = 0.5      # spacing in wavelengths
beta = np.pi / 2  # phase shift to steer beam to 90°

# Compute array factor (beamforming pattern)
numerator = np.sin(N * np.pi * d * np.cos(theta) - beta)
denominator = N * np.sin(np.pi * d * np.cos(theta) - beta)
r = np.abs(numerator / denominator)

# Plot beamforming result in polar coordinates
plt.figure()
plt.polar(theta, r)
plt.title("Beamforming Pattern (Steered to 90°)")
plt.show()
