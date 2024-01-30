import matplotlib.pyplot as plt
import numpy as np

# Données de test
x = np.array([0, 28, 56, 84, 112, 140, 168, 196, 224,
              0, 28, 56, 84, 112, 140, 168, 196, 224,
              0, 28, 56, 84, 112, 140, 168, 196, 224,
              0, 28, 56, 84, 112, 140, 168, 196, 224,
              0, 28, 56, 84, 112, 140, 168, 196, 224])

y = np.array([16, 16, 16, 16, 16, 16, 16, 16, 16,
              32, 32, 32, 32, 32, 32, 32, 32, 32,
              48, 48, 48, 48, 48, 48, 48, 48, 48,
              64, 64, 64, 64, 64, 64, 64, 64, 64,
              80, 80, 80, 80, 80, 80, 80, 80, 80])

error = np.array([35.17, 22.02, 4.12, 2.23, 2.11, 2, 10, 8.94, 12.72,
                  47.63, 21.21, 11.04, 3.60, 8.06, 2.82, 5.09, 4.47, 11.18,
                  45, 30.87, 18.43, 6.08, 2.82, 2.23, 5.09, 5.65, 8.60,
                  55.17, 39, 13, 5.09, 0.63, 2.82, 4, 8.60, 5.09,
                  56.58, 38.47, 22.20, 3.16, 6.40, 8.06, 9.05, 10, 12.36])

error2 = np.array([10.00, 16.64, 14.87, 16.12, 13.04, 10.00, 14.32, 18.00, 20.40,
                   12.81, 13.00, 12.04, 12.04, 7.62, 2.24, 7.28, 8.94, 10.05,
                   12.81, 12.08, 9.49, 8.54, 7.00, 3.16, 3.16, 8.00, 6.08,
                   16.49, 12.04, 13.60, 10.00, 5.10, 4.12, 4.47, 5.10, 10.00,
                   19.70, 17.00, 17.89, 9.00, 9.06, 5.39, 2.24, 6.40, 8.54])

x_lamp = np.array([80, 200, 140])
y_lamp = np.array([70, 77, 185])
error_lamp = np.array([50, 50, 50])

Vmoy_err = np.mean(error)
Vmoy_err2 = np.mean(error2)

# Création de la grille de coordonnées
coords = np.indices(x.shape)

# Coordonnées X de la grille
grid_x = x[coords[0]]

# Coordonnées Y de la grille
grid_y = y[coords[0]]

# Créer la figure et les axes 3D
fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')

# Tracer l'histogramme 3D
colors = [plt.cm.jet(val) for val in (error-np.min(error))/(np.max(error)-np.min(error))]
img = ax.bar3d(grid_x.ravel(), grid_y.ravel(), np.zeros_like(grid_x).ravel(),
         5, 4, error.ravel(), color=colors)

ax.set_box_aspect([12, 10, 5])

for i in range(len(x)):
    ax.text(x[i]+0.5, y[i]+0.5, error[i]+5, str(error[i]), color='black', fontsize=8)

ax.set_xlim3d(0, 280)
ax.set_ylim3d(0, 200)

ax.bar3d(x_lamp, y_lamp, 0, 5, 4, error_lamp, color='yellow')
ax.text(x_lamp[0]-15, y_lamp[0], error_lamp[0]+2, "lamp1", color='black', fontsize=10)
ax.text(x_lamp[1]-15, y_lamp[1], error_lamp[1]+2, "lamp2", color='black', fontsize=10)
ax.text(x_lamp[2]-15, y_lamp[2], error_lamp[2]+2, "lamp3", color='black', fontsize=10)

# Ajouter des étiquettes aux axes
ax.set_title('Distance error old equations')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Distance Error')

ax.text(1.2, 0.5, 0.5, f"The average value is  : {Vmoy_err}", transform=ax.transAxes, fontsize=10)

# Créer la figure et les axes 3D
fig = plt.figure(2)
ax = fig.add_subplot(111, projection='3d')

# Tracer l'histogramme 3D
colors = [plt.cm.jet(val) for val in (error2-np.min(error2))/(np.max(error2)-np.min(error2))]
img = ax.bar3d(grid_x.ravel(), grid_y.ravel(), np.zeros_like(grid_x).ravel(),
         5, 4, error2.ravel(), color=colors)

ax.set_box_aspect([12, 10, 5])

for i in range(len(x)):
    ax.text(x[i]+0.5, y[i]+0.5, error2[i]+5, str(error2[i]), color='black', fontsize=8)

ax.set_xlim3d(0, 280)
ax.set_ylim3d(0, 200)

ax.bar3d(x_lamp, y_lamp, 0, 5, 4, error_lamp, color='yellow')
ax.text(x_lamp[0]-15, y_lamp[0], error_lamp[0]+2, "lamp1", color='black', fontsize=10)
ax.text(x_lamp[1]-15, y_lamp[1], error_lamp[1]+2, "lamp2", color='black', fontsize=10)
ax.text(x_lamp[2]-15, y_lamp[2], error_lamp[2]+2, "lamp3", color='black', fontsize=10)

# Ajouter des étiquettes aux axes
ax.set_title('Distance error new equations')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Distance Error')

ax.text(1.2, 0.5, 0.5, f"The average value is  : {Vmoy_err2}", transform=ax.transAxes, fontsize=10)

# Afficher le graphique
plt.show()
