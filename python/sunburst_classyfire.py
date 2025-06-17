import plotly.express as px
import pickle

with open('ml_inchikey_classyfire.pkl', 'rb') as f:
    ml_inchikey_classyfire = pickle.load(f)

with open('mw_inchikey_classyfire.pkl', 'rb') as f:
    mw_inchikey_classyfire = pickle.load(f)

with open('intersection_classyfire.pkl', 'rb') as f:
    intersection_classyfire = pickle.load(f)

with open('ml_only_classyfire.pkl', 'rb') as f:
    ml_only_classyfire = pickle.load(f)

with open('mw_only_classyfire.pkl', 'rb') as f:
    mw_only_classyfire = pickle.load(f)

fig = px.sunburst(ml_inchikey_classyfire, path=['kingdom', 'super_class', 'class'], values=None, color='super_class')
fig.write_image("testpltly.png")
