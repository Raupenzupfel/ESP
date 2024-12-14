# Beladungskurve Plotten
# Johannes Tadeus Ranisch
# 29.11.2024

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator)

## Import
Ladung = pd.read_excel("C:/Users/tadeu/Documents/0 Studium/Master/1. Semester/ESP-PÜ/Git/MHS/python/RawData/geasamt.xlsx", usecols='A:F',sheet_name='Ladung')

Speicheer_Leer = 6.489
Masse = Ladung[Ladung['m'].notnull()]
## Plotten
fig, ax = plt.subplots()
ax2, ax3, ax4 = ax.twinx(), ax.twinx(), ax.twinx()

fig.subplots_adjust(left=0.001)

ax3.yaxis.set_ticks_position('left')
ax3.yaxis.set_label_position('left')
ax3.spines['left'].set_position(('axes', -0.12))

ax4.set_axis_off()

# ax4.yaxis.set_ticks_position('right')
# ax4.yaxis.set_label_position('right')
# ax4.spines['right'].set_position(('axes', 1.15))

ax.set_xlabel('Zeit in Minuten')
ax.set_ylabel('Druck in bar')
ax.set_title('Beladungsverlauf')
ax2.set_ylabel('Temperatur in °C')
ax3.set_ylabel(r'Volumenstrom in $\frac{Nl}{min}$')

ax.xaxis.set_minor_locator(MultipleLocator(0.5))
ax.grid()

ax.plot(Ladung['t_m'],Ladung['p'], c = '#76B900', label='Druck')
ax2.plot(Ladung['t_m'],Ladung['T'], c='#0082D1', label='Temperatur')
ax3.plot(Ladung['t_m'],Ladung['V'], c='#FF5F00', label='Volumenstrom')
ax4.scatter(Ladung['t_m'],Ladung['m'], c='Black', label=r'$H_2$ Masse')

ax.axvline(0, c='Black', ls=':')
ax.axvline(5, c='Black', ls=':')
ax.axvline(13, c='Black', ls=':')
ax.axvline(21.5, c='Black', ls=':')
ax.axvline(33, c='Black', ls=':')

# ax.text(0.5, 20, r'$\dot{V}=5\frac{Nl}{min}$')
# ax.text(7, 20, r'$\dot{V}=15\frac{Nl}{min}$')
ax.text(17.5, 19, 'Abkühlen\nohne\nBeladung', ha='center')
for i, txt in enumerate(Ladung['m']):
    txt = (Ladung['m'][i]-Speicheer_Leer)*1000
    txt_formatted = "{:.1f}".format(txt)
    ax4.annotate(txt_formatted + ' g', (Ladung['t_m'][i]+0.5, Ladung['m'][i]+0.00045))

# ax.text(22, 20, r'Eisbad mit $\dot{V}=15\frac{Nl}{min}$')

ax.set_xlim(-1, 36.5)
ax.set_ylim(0, 22.5)
ax3.set_ylim(0, 17.5)
ax4.set_ylim(6.485, 6.525)

fig.legend(bbox_to_anchor=(0.52, 0.35))

plt.show()

## Output
fig.savefig('Beladungskurve.svg', bbox_inches = 'tight')
fig.savefig('Beladungskurve.png', bbox_inches = 'tight', dpi=500)