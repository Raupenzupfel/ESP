# ESP PÜ Laufradspeicherversuch - Auslaufzeit Plotten und Analysieren
# Erstellt am 20.11.2024
# Johannes Tadeus Ranisch

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os

os.chdir('C:/Users/tadeu/Documents/0 Studium/Master/1. Semester/ESP-PÜ/Git/Laufradspeicher/python')

## Variablen
Data = "./RawData/20241120_Auslaufzeit.csv"         # relativer Path zur .csv Datei

## Import
Ohne = pd.read_csv(Data, sep=";", usecols=[0,1], skipfooter=13, engine="python", decimal=",")
Mit = pd.read_csv(Data, sep=";", usecols=[6,7], decimal=",")


## Curve Fitting
Fit_sys_mit = np.polyfit(Mit['zeit_mit'],Mit['n_mit'],2)
Fit_sys_ohne = np.polyfit(Ohne['zeit_ohne'],Ohne['n_ohne'],2)

Fit_mit = np.polyval(Fit_sys_mit, Mit['zeit_mit'])
Fit_ohne = np.polyval(Fit_sys_ohne, Mit['zeit_mit'][0:44])

Fit_line_sys_mit = np.polyfit(Mit['zeit_mit'][0:2], Fit_mit[0:2], 1)
Fit_line_sys_ohne = np.polyfit(Mit['zeit_mit'][0:2], Fit_ohne[0:2], 1)

Fit_line_mit = np.polyval(Fit_line_sys_mit, Mit['zeit_mit'])
Fit_line_ohne = np.polyval(Fit_line_sys_ohne, Mit['zeit_mit'])

## Rechnen
# Todo: 
# schnittpunkt mit x-Achse berechnen

mit_line_0 = -Fit_line_sys_mit[1]/Fit_line_sys_mit[0]
ohne_line_0 = -Fit_line_sys_ohne[1]/Fit_line_sys_ohne[0]

mit_0 = (-Fit_sys_mit[1]-np.sqrt((Fit_sys_mit[1]**2) - (4 * Fit_sys_mit[0] * Fit_sys_mit[2])))/(2*Fit_sys_mit[0])
ohne_0 = (-Fit_sys_ohne[1]-np.sqrt((Fit_sys_ohne[1]**2) - (4 * Fit_sys_ohne[0] * Fit_sys_ohne[2])))/(2*Fit_sys_ohne[0])

ticks_mit = [mit_line_0, mit_0]
ticks_ohne = [ohne_line_0, ohne_0]


## Plotten
fig, ax = plt.subplots()
ax2 = ax.twiny()
ax3 = ax.twiny()

ax.grid(True)
ax.set_xlim([0,50])
ax.set_ylim([0,1550])

ax.set_xlabel('Zeit in s', labelpad=30)
ax.set_ylabel('Drehzahl in rpm')
ax.set_title('Auslaufkurven mit und ohne Schwungmasse')

ax.plot(Ohne['zeit_ohne'],Ohne['n_ohne'], label='Ohne Schwungmasse', c="limegreen")
ax.plot(Mit['zeit_mit'][0:44], Fit_ohne, label='Ohne Schwungmasse Fitted', linestyle='dotted', c="limegreen")
ax.plot(Mit['zeit_mit'], Fit_line_ohne, linestyle='dashed', c='limegreen')

ax.plot(Mit['zeit_mit'],Mit['n_mit'], label='Mit Schwungmasse', c="seagreen")
ax.plot(Mit['zeit_mit'], Fit_mit, label='Mit Schwungmasse Fitted', linestyle='dotted', c="seagreen")
ax.plot(Mit['zeit_mit'], Fit_line_mit, linestyle='dashed', c='seagreen')

ax2.set_xlim(ax.get_xlim())
ax2.xaxis.set_ticks_position('bottom')
ax2.xaxis.set_label_position('bottom')
ax2.tick_params(axis='x', length=28, width=1.5)
ax2.set_xticks(ticks_mit)
ax2.set_xticklabels([r'$T_{Aus,mit} = %.2f$' % mit_line_0, r'$%.2f$' % mit_0])
ax2.tick_params(colors='seagreen')

ax3.set_xlim(ax.get_xlim())
ax3.xaxis.set_ticks_position('bottom')
ax3.xaxis.set_label_position('bottom')
ax3.tick_params(axis='x', length=18, width=1.5)
ax3.set_xticks(ticks_ohne)
ax3.set_xticklabels([r'$T_{Aus,ohne} = %.2f$' % ohne_line_0, r'$%.2f$' % ohne_0])
ax3.tick_params(colors='limegreen')

ax.legend()

plt.show()

## Output
fig.savefig('Auslaufkurven.svg', bbox_inches = 'tight')
fig.savefig('Auslaufkurven.png', bbox_inches = 'tight', dpi=500)