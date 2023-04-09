import matplotlib.pyplot as plt
import numpy as np
from projects import projects

colors = ['#0069f5', '#ff7800', '#23a802', '#ff0026']
fig, ax = plt.subplots()
i = 0
for index, project in enumerate(projects):
  data = project['psc'][['psc']]
  x = [int(float(str(i).replace(' ', ''))) if str(i).replace(' ', '') else 120 for i in data['psc']]

  x += [140 for i in x]
  unique, counts = np.unique(x, return_counts=True)
  y = [j + i for j in np.zeros_like(unique)]

  sizes = [i for i in counts]
  
  scatter = ax.scatter(y, unique, s=sizes, alpha=0.6, c=colors[i])
  ax.set_yticks([0, 20, 40, 60, 80, 100, 120, 140])
  ax.set_yticklabels([0, 20, 40, 60, 80, 100, 'Indefinido', 'Total'])
  
  for k, l in enumerate(unique):
    if sizes[k] >= 40 and l not in (120, 140):
      ax.annotate(sizes[k], (i, list(unique)[k]), xytext=(i+0.2, list(unique)[k]-2.5))
    

  total_index = next(i for i, x in enumerate(unique) if x == 140)
  undefined_index = next(i for i, x in enumerate(unique) if x == 120)
  ax.annotate(sizes[total_index], (i, list(unique)[total_index]), xytext=(i+0.2, list(unique)[total_index]-2.5))
  ax.annotate(sizes[undefined_index], (i, list(unique)[undefined_index]),  xytext=(i+0.2, list(unique)[undefined_index]-2.5))
  i += 1

ax.set_xticks([i for i, _ in enumerate(projects)])
ax.set_xticklabels([project['name'] for project in projects])
# Set the label for the x-axis
ax.set_ylabel('PSC (%)')
ax.set_xlim(-1, 4)
ax.set_ylim(-10, 155)
fig.set_size_inches(9, 5)

# Create a legend with a label for each unique value in the 'x' array

plt.savefig('psc.png', dpi=150)
plt.close()