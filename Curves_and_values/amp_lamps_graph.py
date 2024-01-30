import matplotlib.pyplot as plt
import numpy as np

L1, L2, L3=[],[],[]

with open("amp_lamps.txt", "r") as dataFile:
    for l in dataFile:
        data=[str(d) for d in l.split(";")]
        L1i,L2i,L3i = float(data[0]),float(data[1]),float(data[2])
        L1.append(L1i), L2.append(L2i), L3.append(L3i)

L1_10, L2_10, L3_10=[],[],[]

with open("amp_lamps_10.txt", "r") as dataFile:
    for l in dataFile:
        data=[str(d) for d in l.split(";")]
        L1i_10,L2i_10,L3i_10 = float(data[0]),float(data[1]),float(data[2])
        L1_10.append(L1i_10), L2_10.append(L2i_10), L3_10.append(L3i_10)

L1_20, L2_20, L3_20=[],[],[]

with open("amp_lamps_20.txt", "r") as dataFile:
    for l in dataFile:
        data=[str(d) for d in l.split(";")]
        L1i_20,L2i_20,L3i_20 = float(data[0]),float(data[1]),float(data[2])
        L1_20.append(L1i_20), L2_20.append(L2i_20), L3_20.append(L3i_20)


L1_30, L2_30, L3_30=[],[],[]

with open("amp_lamps_30.txt", "r") as dataFile:
    for l in dataFile:
        data=[str(d) for d in l.split(";")]
        L1i_30,L2i_30,L3i_30 = float(data[0]),float(data[1]),float(data[2])
        L1_30.append(L1i_30), L2_30.append(L2i_30), L3_30.append(L3i_30)
#print("nombre de points total dans le fichier texte = ", len(L1))
#for i in range (0,582):
#    print(L1[i],L2[i],L3[i])

plt.figure(1)

plt.plot(L1)
plt.plot(L2)
plt.plot(L3)

plt.grid(True)

plt.figure(2)

plt.plot(L1_10)
plt.plot(L2_10)
plt.plot(L3_10)

plt.grid(True)

plt.figure(3)

plt.plot(L1_20)
plt.plot(L2_20)
plt.plot(L3_20)

plt.grid(True)

plt.figure(4)

plt.plot(L1_30)
plt.plot(L2_30)
plt.plot(L3_30)

plt.grid(True)

plt.show()