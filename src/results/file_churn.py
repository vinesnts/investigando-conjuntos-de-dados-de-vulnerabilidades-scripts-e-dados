import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import trim_mean

from projects import projects

def categorize(values):
  cc_qtds = {0: 0, 1: 0, 2: 0, 3: 0}
  for i in values:
    if i == 0:
      cc_qtds[i] += 1
    elif i == 1:
      cc_qtds[i] += 1
    elif i == 2:
      cc_qtds[i] += 1
    elif i >= 3:
      cc_qtds[3] += 1
  return cc_qtds

def quantities(values):
  cc_qtds = {}
  for i in values:
    if i not in cc_qtds:
      cc_qtds[i] = 0
    cc_qtds[i] += 1
  return cc_qtds

cores = ['red', 'blue', 'green', 'orange']

for project in projects:
  cc = project['file_churn'][['file_churn']]

  print(f"Projeto {project['name']}")
  print(f"Média: {np.mean(np.array(cc))}")
  print(f"Mediana: {np.median(np.array(cc))}")
  print(f"Máx.: {np.max(np.array(cc))}")
  print(f"Mín.: {np.min(np.array(cc))}")
  print(f"Média aparada.: {trim_mean(np.array(cc), 0.1)}")

  fig, ax = plt.subplots(1,1)
  ax.set_title(f"Métrica Code Churn - Projeto {project['name']}")

  cc_qtds = categorize(cc['file_churn'])
  print(cc_qtds)
  ax.pie(cc_qtds.values(), labels=[cc_qtds[i] for i in cc_qtds.keys()], colors=['#3388ff', '#FFBABA', '#FF7B7B', '#FF5252'])
  ax.legend([i if i < 3 else '3 ou mais' for i in cc_qtds.keys()], loc='lower right')
  plt.savefig(f'cc-{project["name"]}.png')
  plt.close()