import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Function to compute the derivatives of the system
def derivs(y, t, l, g):
    theta, omega = y
    dydt = [omega, -g / l * np.sin(theta)]
    return dydt

# Initial conditions
y0 = [np.pi / 4, 0]  # Initial angle and angular velocity

# Time grid
t = np.linspace(0, 10, 1000)

# Pendulum parameters
l = 1.0  # Length of pendulum arm
g = 9.8  # Acceleration due to gravity

# Solve the ODE
sol = odeint(derivs, y0, t, args=(l, g))

# Plot the pendulum motion
plt.plot(l * np.sin(sol[:, 0]), -l * np.cos(sol[:, 0]))
plt.title('Simple Pendulum Motion')
plt.xlabel('Horizontal Displacement')
plt.ylabel('Vertical Displacement')
plt.axis('equal')
plt.show()
