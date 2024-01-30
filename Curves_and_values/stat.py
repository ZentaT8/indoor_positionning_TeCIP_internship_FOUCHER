import matplotlib.pyplot as plt
import numpy as np

expectedX = 200
expectedY = 29

expectedX_2 = 127
expectedY_2 = 50

PosX, PosY=[],[]

with open("test_stat.txt", "r") as dataFile:
    for l in dataFile:
        data=[str(d) for d in l.split(", ")]
        PosXi, PosYi = float(data[0]),float(data[1])
        PosX.append(PosXi), PosY.append(PosYi)

VmoyX = np.mean(PosX)
VmoyY = np.mean(PosY)

plt.figure(1)
plt.hist(PosX, edgecolor = 'black', alpha=0.5, color='red')
plt.hist(expectedX, color='lightgreen')
plt.hist(VmoyX, color='blue')
plt.title('Position X')
plt.xlabel('Position in cm')
plt.ylabel('frequency of occurrence')

plt.figure(2)
plt.hist(PosY, edgecolor = 'black', alpha=0.5, color='red')
plt.hist(expectedY, color='lightgreen')
plt.hist(VmoyY, color='blue')
plt.title('Position Y')
plt.xlabel('Position in cm')
plt.ylabel('frequency of occurrence')

PosX_20, PosY_20=[],[]

with open("test_stat_20.txt", "r") as dataFile:
    for l in dataFile:
        data=[str(d) for d in l.split(",")]
        PosXi_20, PosYi_20 = float(data[0]),float(data[1])
        PosX_20.append(PosXi_20), PosY_20.append(PosYi_20)

VmoyX_20 = np.mean(PosX_20)
VmoyY_20 = np.mean(PosY_20)

plt.figure(3)
plt.hist(PosX_20, edgecolor = 'black', alpha=0.5, color='red')
plt.hist(expectedX_2, color='lightgreen')
plt.hist(VmoyX_20, color='blue')
plt.title('Position X')
plt.xlabel('Position in cm')
plt.ylabel('frequency of occurrence')

plt.figure(4)
plt.hist(PosY_20, edgecolor = 'black', alpha=0.5, color='red')
plt.hist(expectedY_2, color='lightgreen')
plt.hist(VmoyY_20, color='blue')
plt.title('Position Y')
plt.xlabel('Position in cm')
plt.ylabel('frequency of occurrence')

plt.show()