import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to compute the derivatives of the system
def derivs(y, t, l1, l2, m1, m2, g):
    theta1, omega1, theta2, omega2 = y

    c, s = np.cos(theta1 - theta2), np.sin(theta1 - theta2)
    det = m1 * m2 * l1**2 * l2**2 - 2 * m2 * l1 * l2 * (m1 + m2 * (1 - c**2))

    dydt = [
        omega1,
        (m2 * l2 * omega2**2 * s + m2 * g * np.sin(theta2) - (m1 + m2) * g * np.sin(theta1)) / (l1 * det),
        omega2,
        ((m1 + m2) * l1 * omega1**2 * s - (m1 + m2) * g * np.sin(theta1) + m2 * g * np.sin(theta2)) / (l2 * det)
    ]

    return dydt

# Initial conditions
y0 = [np.pi / 4, 0, np.pi / 2, 0]  # Initial angles and angular velocities

# Time grid
t = np.linspace(0, 10, 1000)

# Pendulum parameters
l1, l2 = 1.0, 1.0  # Length of pendulum arms
m1, m2 = 1.0, 1.0  # Masses
g = 9.8  # Acceleration due to gravity

# Solve the ODE
sol = odeint(derivs, y0, t, args=(l1, l2, m1, m2, g))

# Animation function for visualization
def animate(i):
    plt.clf()
    x1 = l1 * np.sin(sol[i, 0])
    y1 = -l1 * np.cos(sol[i, 0])
    x2 = x1 + l2 * np.sin(sol[i, 2])
    y2 = y1 - l2 * np.cos(sol[i, 2])

    plt.plot([0, x1, x2], [0, y1, y2], marker='o')
    plt.xlim([-2, 2])
    plt.ylim([-2, 2])

# Create an animation
ani = FuncAnimation(plt.gcf(), animate, frames=len(t), interval=20, blit=False)
plt.show()

#Terminal (cd ~/Downloads/Pendulums) self example (Basically, just set the path)
#To run use python3 Double_Pendulum.py (for zsh, BASH is different for Vscode)
