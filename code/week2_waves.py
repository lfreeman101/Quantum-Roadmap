# Week 2: Sine + Cosine interference demo
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4*np.pi, 1000)
y1 = np.sin(x)
y2 = np.cos(x)
y_sum = y1 + y2

plt.plot(x, y1, label="sin(x)")
plt.plot(x, y2, label="cos(x)")
plt.plot(x, y_sum, label="sin(x)+cos(x)")
plt.legend()
plt.xlabel("x")
plt.ylabel("amplitude")
plt.title("Interference: sin + cos")
plt.show()
