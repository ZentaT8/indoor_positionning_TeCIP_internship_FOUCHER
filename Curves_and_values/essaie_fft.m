clear all;
close all;

donnees = load("fft_compute.txt");

N=8192;
Fe=100000;
h=hamming(N);
#h=transpose(h);
x1=donnees.*h;

M=8192;
df=Fe/M;
f=0:df:(Fe)-df;

fft_compute=fft(x1);
abs_fft=abs(fft_compute);
sq_fft=abs_fft.*abs_fft;

subplot(211);
plot(donnees, "b.-");

subplot(212);
plot(f, 10*log10(sq_fft));
