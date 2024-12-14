# Entladungskurve Plotten
# Johannes Tadeus Ranisch
# 29.11.2024

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator)

## Import
Entladung = pd.read_excel("C:/Users/tadeu/Documents/0 Studium/Master/1. Semester/ESP-PÜ/Git/MHS/python/RawData/geasamt.xlsx", usecols='A:F',sheet_name='Entladung')

Speicher_Leer = 6.489
Masse = Entladung[Entladung['m'].notnull()]
print(Masse)

## Plotten
fig, ax = plt.subplots()
ax2, ax3, ax4 = ax.twinx(), ax.twinx(), ax.twinx()

fig.subplots_adjust(left=0.001)

ax3.yaxis.set_ticks_position('left')
ax3.yaxis.set_label_position('left')
ax3.spines['left'].set_position(('axes', -0.12))

ax4.set_axis_off()

ax.set_xlabel('Zeit in Minuten')
ax.set_ylabel('Druck in bar')
ax.set_title('Entladungsverlauf')
ax2.set_ylabel('Temperatur in °C')
ax3.set_ylabel(r'Volumenstrom in $\frac{Nl}{min}$')

ax.xaxis.set_minor_locator(MultipleLocator(0.5))
ax.grid()

ax.plot(Entladung['t_m'],Entladung['p'], c = '#76B900', label='Druck')
ax2.plot(Entladung['t_m'],Entladung['T'], c='#0082D1', label='Temperatur')
ax3.plot(Entladung['t_m'],Entladung['V'], c='#FF5F00', label='Volumenstrom')
ax4.scatter(Masse['t_m'], Masse['m'], c='Black', label=r'$H_2$ Masse')

ax.axvline(0, c='Black', ls=':')
ax.axvline(5.5, c='Black', ls=':')
ax.axvline(11, c='Black', ls=':')
ax.axvline(16.5, c='Black', ls=':')
ax.axvline(28, c='Black', ls=':')

# ax.text(0.5, 12.5, r'$\dot{V}=5\frac{Nl}{min}$')
# ax.text(6, 12.5, r'$\dot{V}=11\frac{Nl}{min}$')
ax.text(14, 3, 'Erwärmen\nohne\nBeladung', ha='center')
for i, txt in enumerate(Entladung['m']):
    txt = (Entladung['m'][i]-Speicher_Leer)*1000
    txt_formatted = "{:.1f}".format(txt)
    ax4.annotate(txt_formatted + ' g', (Entladung['t_m'][i]+0.5, Entladung['m'][i]-0.0003))
# ax.text(17, 4, r'Heißwasserbad mit $\dot{V}=11\frac{Nl}{min}$')

ax.set_xlim(-1, 30.5)
ax.set_ylim(0, 22.5)
ax3.set_ylim(0, 17.5)

fig.legend(bbox_to_anchor=(0.8, 0.4))

plt.show()

## Output
fig.savefig('Entladungskurve.svg', bbox_inches = 'tight')
fig.savefig('Entladungskurve.png', bbox_inches = 'tight', dpi=500)