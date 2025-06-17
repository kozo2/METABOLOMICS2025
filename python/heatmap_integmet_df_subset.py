import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

with open('integmet_df_subset.pkl', 'rb') as f:
    df = pickle.load(f)

plt.figure()
sns.heatmap(df, cmap="crest", xticklabels=False, yticklabels=False)
plt.savefig("heatmap_integmet_df_subset.png")
plt.close()
