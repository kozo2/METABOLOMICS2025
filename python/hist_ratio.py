import numpy as np
import pickle
import matplotlib.pyplot as plt

with open('ratio_values.pkl', 'rb') as f:
    arr = pickle.load(f)

log2_arr = np.where(arr > 0, np.log2(arr), np.nan)
bin_edges = np.arange(-18, 18 + 0.5, 0.5)
plt.figure()
plt.hist(log2_arr, bins=bin_edges, edgecolor='black')

# plt.axvline(x=-1.5, color='red', linestyle='--', linewidth=2, label='Threshold = -1.5')
# plt.axvline(x=1.5, color='red', linestyle='--', linewidth=2, label='Threshold = 1.5')

plt.xlabel('')
plt.ylabel('')
plt.title('')
plt.grid(True, alpha=0.3)
# plt.grid(True)

#plt.savefig("hist_fc.png", dpi=300, bbox_inches='tight')
plt.savefig("hist_log2_ratio_no_thre.png", dpi=300, bbox_inches='tight')

plt.close()
