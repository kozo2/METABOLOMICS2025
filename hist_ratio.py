import numpy as np

with open('ratio_values.pkl', 'rb') as f:
    arr = pickle.load(f)

bin_edges = np.arange(-6, 6 + 0.1, 0.1)
plt.figure()
plt.hist(arr, bins=bin_edges, edgecolor='black')

plt.xlabel('')
plt.ylabel('')
plt.title('')
plt.grid(True)

plt.savefig("hist_fc.png", dpi=300, bbox_inches='tight')
plt.close()
