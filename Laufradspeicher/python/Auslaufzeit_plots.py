# ESP PÜ Laufradspeicherversuch - Auslaufzeit Plotten und Analysieren
# Erstellt am 20.11.2024
# Johannes Tadeus Ranisch

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

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
#   Für line
#       diese als extraticks markieren
#   Für Fit als argumentationsgrundlage Protokoll

## Plotten
fig, ax = plt.subplots()

ax.grid(True)
ax.set_xlim([0,50])
ax.set_ylim([0,1550])
# plt.xticks(list(plt.xticks()[0]) + extraticks)

ax.set_xlabel('Zeit in s')
ax.set_ylabel('Drehzahl in rpm')
ax.set_title('Auslaufkurven mit und ohne Schwungmasse')

ax.plot(Ohne['zeit_ohne'],Ohne['n_ohne'], label='Ohne Schwungmasse', c="green")
ax.plot(Mit['zeit_mit'][0:44], Fit_ohne, label='Ohne Schwungmasse Fitted', linestyle='dotted', c="green")
ax.plot(Mit['zeit_mit'], Fit_line_ohne, linestyle='dashed', c='green')

ax.plot(Mit['zeit_mit'],Mit['n_mit'], label='Mit Schwungmasse', c="lightgreen")
ax.plot(Mit['zeit_mit'], Fit_mit, label='Mit Schwungmasse Fitted', linestyle='dotted', c="lightgreen")
ax.plot(Mit['zeit_mit'], Fit_line_mit, linestyle='dashed', c='lightgreen')

ax.legend()

plt.show()