import glob
import pandas as pd

mwtsvs = glob.glob("AN*.tsv")
mwratios = []
for i in mwtsvs:
    df = pd.read_csv(i, sep='\t', index_col=0)
    first_col = df.iloc[:, 0]
    mwratios.append(first_col)

giantmw = pd.concat(mwratios, axis=1)
giantmw.to_pickle("all_mw_ratio.pkl")

giantmw.index.to_series().to_csv("mw_inchikeys.txt", index=False, header=False)

integmet_df = pd.concat([giantml, giantmw], axis=1)
non_nan_counts = integmet_df.notna().sum(axis=1)
filtered_values = all_values[~np.isnan(all_values)]
