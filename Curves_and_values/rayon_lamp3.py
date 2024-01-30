import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Données de test
x_l1 = np.array([25, 38, 60, 85, 136, 143])
y_l1 = np.array([70, 34, 17, 11, 44, 70])
amp_dB_l1 = np.array([26.15, 26.5, 26.9, 27, 26, 26])

x_l2 = np.array([140, 149, 174, 203, 236, 260])
y_l2 = np.array([70, 41, 19, 13, 23, 70])
amp_dB_l2 = np.array([25, 25.6, 26.2, 26.2, 26.2, 26])

x = np.array([60, 84, 102, 134, 175, 202])
y = np.array([70, 58, 52 ,52 ,57 ,69])
amp_dB = np.array([22.22, 22.65, 23, 23.7, 24.22, 24.5])

x_lamp = np.array([85, 200, 140])
y_lamp = np.array([70, 70, 185])
amp_db_lamp = np.array([28, 28, 31.2])

# Création de la grille de coordonnées
coords = np.indices(x.shape)

# Coordonnées X de la grille
grid_x = x[coords[0]]
grid_x_l1 = x_l1[coords[0]]
grid_x_l2 = x_l2[coords[0]]

# Coordonnées Y de la grille
grid_y = y[coords[0]]
grid_y_l1 = y_l1[coords[0]]
grid_y_l2 = y_l2[coords[0]]

####################################################Lamp 3#####################################################

# Créer la figure et les axes 3D
fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')

# Tracer l'histogramme 3D
colors = [plt.cm.jet(val) for val in (amp_dB-np.min(amp_dB))/(np.max(amp_dB)-np.min(amp_dB))]
img = ax.bar3d(grid_x.ravel(), grid_y.ravel(), np.zeros_like(grid_x).ravel(),
         5, 5, amp_dB.ravel(), color=colors)

ax.bar3d(x_lamp[2], y_lamp[2], 0, 5, 5, amp_db_lamp[0], color='yellow')
ax.text(x_lamp[2]-15, y_lamp[2], amp_db_lamp[2]+2, "lamp3", color='black', fontsize=10)

ax.set_box_aspect([12, 10, 5])
ax.set_xlim3d(0, 280)
ax.set_ylim3d(0, 200)
for i in range(len(x)):
    ax.text(x[i]+0.5, y[i]+0.5, amp_dB[i]+5, str(amp_dB[i]), color='black', fontsize=10)

# Ajouter des étiquettes aux axes
ax.set_title('Lamp 3 beam at 140cm')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Amplitude dB')

########################################################Lamp 1#####################################################
fig = plt.figure(2)
ax = fig.add_subplot(111, projection='3d')

# Tracer l'histogramme 3D
colors = [plt.cm.jet(val) for val in (amp_dB_l1-np.min(amp_dB_l1))/(np.max(amp_dB_l1)-np.min(amp_dB_l1))]
img = ax.bar3d(grid_x_l1.ravel(), grid_y_l1.ravel(), np.zeros_like(grid_x_l1).ravel(),
         5, 5, amp_dB_l1.ravel(), color=colors)

ax.bar3d(x_lamp[0], y_lamp[0], 0, 5, 5, amp_db_lamp[0], color='yellow')
ax.text(x_lamp[0]-15, y_lamp[0], amp_db_lamp[0]+2, "lamp1", color='black', fontsize=10)

ax.set_box_aspect([12, 10, 5])
ax.set_xlim3d(0, 280)
ax.set_ylim3d(0, 200)
for i in range(len(x_l1)):
    ax.text(x_l1[i]+0.5, y_l1[i]+0.5, amp_dB_l1[i]+5, str(amp_dB_l1[i]), color='black', fontsize=10)

# Ajouter des étiquettes aux axes
ax.set_title('Lamp 1 beam at 60cm')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Amplitude dB')

########################################################Lamp 2#####################################################
fig = plt.figure(3)
ax = fig.add_subplot(111, projection='3d')

# Tracer l'histogramme 3D
colors = [plt.cm.jet(val) for val in (amp_dB_l2-np.min(amp_dB_l2))/(np.max(amp_dB_l2)-np.min(amp_dB_l2))]
img = ax.bar3d(grid_x_l2.ravel(), grid_y_l2.ravel(), np.zeros_like(grid_x_l2).ravel(),
         5, 5, amp_dB_l2.ravel(), color=colors)

ax.bar3d(x_lamp[1], y_lamp[1], 0, 5, 5, amp_db_lamp[1], color='yellow')
ax.text(x_lamp[1]-15, y_lamp[1], amp_db_lamp[1]+2, "lamp2", color='black', fontsize=10)

ax.set_box_aspect([12, 10, 5])
ax.set_xlim3d(0, 280)
ax.set_ylim3d(0, 200)
for i in range(len(x_l2)):
    ax.text(x_l2[i]+0.5, y_l2[i]+0.5, amp_dB_l2[i]+5, str(amp_dB_l2[i]), color='black', fontsize=10)

# Ajouter des étiquettes aux axes
ax.set_title('Lamp 2 beam at 60cm')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Amplitude dB')

# Afficher le graphique
plt.show()
