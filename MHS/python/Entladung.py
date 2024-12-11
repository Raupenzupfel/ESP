# Entladungskurve Plotten
# Johannes Tadeus Ranisch
# 29.11.2024

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator)

## Import
Entladung = pd.read_excel("C:/Users/tadeu/Documents/0 Studium/Master/1. Semester/ESP-PÜ/Git/MHS/python/RawData/geasamt.xlsx", usecols='A:D',sheet_name='Entladung')

## Plotten
fig, ax = plt.subplots()
ax2 = ax.twinx()

ax.set_xlabel('Zeit in Minuten')
ax.set_ylabel('Druck in bar')
ax.set_title('Entladungsverlauf')
ax2.set_ylabel('Temperatur in °C')

ax.xaxis.set_minor_locator(MultipleLocator(0.5))
ax.grid()


ax.plot(Entladung['t_m'],Entladung['p'], c = '#76B900', label='Druck')
ax2.plot(Entladung['t_m'],Entladung['T'], c='#0082D1', label='Temperatur')

ax.axvline(5.5, c='#FF5F00')
ax.axvline(11, c='#FF5F00')
ax.axvline(16.5, c='#FF5F00')

ax.text(0.5, 12.5, r'$\dot{V}=5\frac{Nl}{min}$')
ax.text(6, 12.5, r'$\dot{V}=11\frac{Nl}{min}$')
ax.text(14, 3, 'Erwärmen\nohne\nBeladung', ha='center')
ax.text(17, 4, r'Heißwasserbad mit $\dot{V}=11\frac{Nl}{min}$')

ax.set_xlim(0, 29)
ax.set_ylim(0, 22.5)

fig.legend(bbox_to_anchor=(0.35, 0.88))

plt.show()

## Output
fig.savefig('Entladungskurve.svg', bbox_inches = 'tight')
fig.savefig('Entladungskurve.png', bbox_inches = 'tight', dpi=500)