import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-220, 220, 100)
y2 = -2 * pow(10, -14) * pow(x, 6) - 1 * pow(10, -20) * pow(x, 5) + 7 * pow(10, -9) * pow(x, 4) + 9 * pow(10, -10) * pow(x, 3) - 0.00065 * pow(x, 2) + 8 * pow(10, -11) * x + 27.611
y3 = -2 * pow(10, -14) * pow(x, 6) - 1 * pow(10, -20) * pow(x, 5) + 5 * pow(10, -9) * pow(x, 4) + 8 * pow(10, -16) * pow(x, 3) - 0.0005 * pow(x, 2) + 8 * pow(10, -11) * x + 31.174
y1 = -2 * pow(10, -14) * pow(x, 6) + 5 * pow(10, -21) * pow(x, 5) + 3 * pow(10, -9) * pow(x, 4) + 7 * pow(10, -16) * pow(x, 3) - 0.0005 * pow(x, 2) + 4 * pow(10, -11) * x + 27.791
fig = plt.figure(figsize = (10, 5))
plt.xticks([-220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220])
plt.plot(x, y2)
plt.plot(x, y1)
plt.plot(x, y3)
plt.grid(True)
plt.show()