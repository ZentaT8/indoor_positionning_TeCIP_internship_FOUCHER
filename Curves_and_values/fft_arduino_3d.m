clear all;
close all;

data = load('fft_arduino_3d.txt'); % Charger les données depuis le fichier texte

% Séparer les colonnes des données en variables distinctes
freq = data(:,2);
nb_acq = data(:,1);
ampl = data(:,3);

% Définir la grille régulière pour l'interpolation
N = 4096; 
M = 5;
freq_interp = linspace(min(freq), max(freq), N);
nb_acq_interp = linspace(min(nb_acq), max(nb_acq), M);
[FREQ, NB_ACQ] = meshgrid(freq_interp, nb_acq_interp);

% Effectuer l'interpolation des données d'amplitude
AMPL = griddata(freq, nb_acq, ampl, FREQ, NB_ACQ);

color_set = ([0 0 1 ; 0 0 1 ; 0.1 0.8 1 ; 1 1 0 ; 1 0.6 0 ; 1 0 0]);
                
% Afficher le graphe en 3D
pcolor(FREQ, NB_ACQ, AMPL);
xlim([1000 8000]);
ylim([-90 90]);
yticks([-90 -45 0 45 90]);
zlim([-60 40]);

title('3D graph with change of the angle');
xlabel('Frequency');
ylabel('angle in °');
zlabel('Amplitude');
                
caxis([-20 40]);
colormap(jet(256));
cb = colorbar;
title(cb, 'dB');