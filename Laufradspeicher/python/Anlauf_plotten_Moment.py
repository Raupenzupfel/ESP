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
I_1 = pd.read_csv("./RawData/Anlauf_V1_CH1.csv", skiprows=20)
I_2 = pd.read_csv("./RawData/Anlauf_V2_CH1.csv", skiprows=20)

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
neu_I1 = [0]
neu_I2 = [0]
for i in new_step.astype(int):
    neu_U1.append(U_1['CH3'][i_old:i].mean())
    neu_U2.append(U_2['CH3'][i_old:i].mean())
    neu_n1.append(n_1['CH2'][i_old:i].mean()*50)
    neu_n2.append(n_2['CH2'][i_old:i].mean()*50)
    neu_I1.append(I_1['CH1'][i_old:i].mean())
    neu_I2.append(I_2['CH1'][i_old:i].mean())
    i_old = i
    
neu_Time_U1 = [0]
neu_Time_U2 = [0]
neu_Time_n1 = [0]
neu_Time_n2 = [0]
neu_Time_I1 = [0]
neu_Time_I2 = [0]
for i in new_step.astype(int)-1:
    neu_Time_U1.append(U_1['TIME'][i])
    neu_Time_U2.append(U_2['TIME'][i])
    neu_Time_n1.append(n_1['TIME'][i])
    neu_Time_n2.append(n_2['TIME'][i])
    neu_Time_I1.append(I_1['TIME'][i])
    neu_Time_I2.append(I_2['TIME'][i])
    
## Plotten
fig, ax = plt.subplots()
ax2 = ax.twinx()
ax3 = ax.twinx()

fig.subplots_adjust(left=0.001)

ax3.yaxis.set_ticks_position('left')
ax3.yaxis.set_label_position('left')
ax3.spines['left'].set_position(('axes', -0.12))

ax.set_xlabel('Zeit in s')
# ax.set_ylabel('Spannung in V')
ax.set_title('Anlaufkurven')
ax.set_ylabel('Strom in A')
ax2.set_ylabel('Drehzahl in rpm')
ax.grid(True, which='both', axis='both', alpha = .5)

# ax.plot(neu_Time_U1, neu_U1, label='Spannung 1', c='darkgreen')
# ax.plot(neu_Time_U2, neu_U2, label='Spannung 2', c='lime')
ax.plot(neu_Time_I1, neu_I1, label='Strom 1', c='darkblue')
ax.plot(neu_Time_I2, neu_I2, label='Strom 2', c='dodgerblue')
ax2.plot(neu_Time_n1, neu_n1, label='Drehzahl 1', c='darkorange')   
ax2.plot(neu_Time_n2, neu_n2, label='Drehzahl 2', c='gold')
ax.set_xlim([0,1])

# ax.set_ylim([0,max(neu_U1)*1.05])
ax.set_ylim([0,max(neu_I1)*1.05])
ax2.set_ylim([0,max(neu_n1)*1.05])

print(max(I_1['CH1']), max(I_2['CH1']))

fig.legend(bbox_to_anchor=(0.68, 0.5), loc='upper left', borderaxespad=0)

plt.show()

## Output
fig.savefig('Anlaufkurven_Moment.svg', bbox_inches = 'tight')
fig.savefig('Anlaufkurven_Moment.png', bbox_inches = 'tight', dpi=500)