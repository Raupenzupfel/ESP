# Darstelölen des Anlaufs
# Johannes Tadeus Ranisch
# 24.11.2024

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

## Import
U_1 = pd.read_csv("./RawData/Anlauf_V1_CH3.csv", skiprows=20)
U_2 = pd.read_csv("./RawData/Anlauf_V2_CH3.csv", skiprows=20)
n_1 = pd.read_csv("./RawData/Anlauf_V1_CH2.csv", skiprows=20)
n_2 = pd.read_csv("./RawData/Anlauf_V2_CH2.csv", skiprows=20)

## Variablen
length = len(U_1['CH3'])
num = 100                               # Anzahle der Punlte in den Linien = len(U_1)/intervall

## Mittelwertbildung der Spannung
new_step = np.linspace(1, length, num)  # 10 20 30 40...
i_old = 0
neu_U1 = [0]
neu_U2 = [0]
neu_n1 = [0]
neu_n2 = [0]
for i in new_step.astype(int):
    neu_U1.append(U_1['CH3'][i_old:i].mean())
    neu_U2.append(U_2['CH3'][i_old:i].mean())
    neu_n1.append(n_1['CH2'][i_old:i].mean()*50)
    neu_n2.append(n_2['CH2'][i_old:i].mean()*50)
    i_old = i
    
neu_Time_U1 = [0]
neu_Time_U2 = [0]
neu_Time_n1 = [0]
neu_Time_n2 = [0]
for i in new_step.astype(int)-1:
    neu_Time_U1.append(U_1['TIME'][i])
    neu_Time_U2.append(U_2['TIME'][i])
    neu_Time_n1.append(n_1['TIME'][i])
    neu_Time_n2.append(n_2['TIME'][i])
    
## Plotten
fig, ax = plt.subplots()
ax2 = ax.twinx()

ax.set_xlabel('Zeit in s')
ax.set_ylabel('Spannung in V')
ax.set_title('Anlaufkurven')
ax2.set_ylabel('Drehzahl in rpm')
ax.grid(True, which='both', axis='both', alpha = .5)

ax.plot(neu_Time_U1, neu_U1, label='Spannung 1', c='darkgreen')
ax.plot(neu_Time_U2, neu_U2, label='Spannung 2', c='lime')
ax2.plot(neu_Time_n1, neu_n1, label='Drehzahl 1', c='darkorange')   
ax2.plot(neu_Time_n2, neu_n2, label='Drehzahl 2', c='gold')
ax.set_xlim([0,1])

fig.legend(bbox_to_anchor=(0.68, 0.31), loc='upper left', borderaxespad=0)

plt.show()

## Output
fig.savefig('Anlaufkurven.svg', bbox_inches = 'tight')
fig.savefig('Anlaufkurven.png', bbox_inches = 'tight', dpi=500)