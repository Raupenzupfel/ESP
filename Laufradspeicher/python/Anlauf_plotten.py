# Darstelölen des Anlaufs
# Johannes Tadeus Ranisch
# 24.11.2024

import pandas as pd
import matplotlib.pyplot as plt

## Variablen


## Import
U_1 = pd.read_csv("./RawData/Anlauf_V1_CH3.csv", skiprows=20)
U_2 = pd.read_csv("./RawData/Anlauf_V2_CH3.csv", skiprows=20)
n_1 = pd.read_csv("./RawData/Anlauf_V1_CH2.csv", skiprows=20)
n_2 = pd.read_csv("./RawData/Anlauf_V2_CH2.csv", skiprows=20)

## Plotten
fig, ax = plt.subplots()
ax2 = ax.twinx()

ax.set_xlabel('SZeit in s')
ax.set_ylabel('Spannung in V')
ax.set_title('Anlaufkurven')
ax2.set_ylabel('Drehzahl in rpm')
ax.grid(True, which='both', axis='both', alpha = .5)

ax.plot(U_1['TIME'], U_1['CH3'], label='Spannung 1')
ax.plot(U_2['TIME'], U_2['CH3'], label='Spannung 2')
ax2.plot(n_1['TIME'], n_1['CH2']*50, label='Drehzahl 1', c='red')   
ax2.plot(n_2['TIME'], n_2['CH2']*50, label='Drehzahl 2', c='g')
ax.set_xlim([0,1])

fig.legend()

plt.show()