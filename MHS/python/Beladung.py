# Beladungskurve Plotten
# Johannes Tadeus Ranisch
# 29.11.2024

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator)

## Import
Ladung = pd.read_excel("C:/Users/tadeu/Documents/0 Studium/Master/1. Semester/ESP-PÜ/Git/MHS/python/RawData/geasamt.xlsx", usecols='A:D',sheet_name='Ladung')

## Plotten
fig, ax = plt.subplots()
ax2 = ax.twinx()

ax.set_xlabel('Zeit in Minuten')
ax.set_ylabel('Druck in bar')
ax.set_title('Beladungsverlauf')
ax2.set_ylabel('Temperatur in °C')

ax.xaxis.set_minor_locator(MultipleLocator(0.5))
ax.grid()


ax.plot(Ladung['t_m'],Ladung['p'], c = '#76B900', label='Druck')
ax2.plot(Ladung['t_m'],Ladung['T'], c='#0082D1', label='Temperatur')

ax.axvline(5, c='#FF5F00')
ax.axvline(13, c='#FF5F00')
ax.axvline(21.5, c='#FF5F00')

ax.text(0.5, 20, r'$\dot{V}=5\frac{Nl}{min}$')
ax.text(7, 20, r'$\dot{V}=15\frac{Nl}{min}$')
ax.text(17.5, 19, 'Abkühlen\nohne\nBeladung', ha='center')
ax.text(22, 20, r'Eisbad mit $\dot{V}=15\frac{Nl}{min}$')

ax.set_xlim(0, 33)
ax.set_ylim(0, 22.5)

fig.legend(bbox_to_anchor=(0.55, 0.3))

plt.show()

## Output
fig.savefig('Beladungskurve.svg', bbox_inches = 'tight')
fig.savefig('Beladungskurve.png', bbox_inches = 'tight', dpi=500)