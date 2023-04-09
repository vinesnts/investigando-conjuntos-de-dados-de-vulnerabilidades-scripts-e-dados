import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from projects import projects

for project in projects:
  nea = project['nea'][['nea']]

  ax = nea.value_counts().plot.pie(colors=['#0069f5', '#ff7800'], autopct='%1.2f%%', legend=True, labels=None, textprops={'fontsize': 15, 'color': 'black'}, pctdistance=1.30)
  ax.get_yaxis().set_visible(False)
  # ax.set_title(f"Métrica NEA - Projeto {project['name']}")
  print(nea.isna().sum())
  plt.legend(['Não', 'Sim'], fontsize='15')
  plt.tight_layout()
  plt.savefig(f'nea-{project["name"]}.png')
  plt.close()