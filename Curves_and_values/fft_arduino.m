clear all;
close all;

donnees = load("fft_arduino.txt");

plot(donnees(:,2), donnees(:,3));
xlim([1000 8000]);
ylim([-20 40]);

title('FFT');
xlabel('Frequency');
ylabel('Amplitude in dB');