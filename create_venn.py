from matplotlib_venn import venn2
import matplotlib.pyplot as plt
import pickle

with open('MetaboLights_InChIKeys.pkl', 'rb') as f:
    ml = pickle.load(f)

with open('MW_InChIKeys.pkl', 'rb') as f:
    mw = pickle.load(f)

mlikeyset = set(ml)
mwikeyset = set(mw)
plt.figure()
v=venn2((mlikeyset, mwikeyset), set_labels=('', ''))
plt.savefig("MLredMWgreen_venn.png")
plt.close()
