import plotly.express as px
from plotly.colors import qualitative
import pickle
import itertools

with open('ml_inchikey_classyfire.pkl', 'rb') as f:
    ml_inchikey_classyfire = pickle.load(f)

with open('mw_inchikey_classyfire.pkl', 'rb') as f:
    mw_inchikey_classyfire = pickle.load(f)

with open('intersection_classyfire.pkl', 'rb') as f:
    intersection_classyfire= pickle.load(f)

with open('ml_only_classyfire.pkl', 'rb') as f:
    ml_only_classyfire = pickle.load(f)

with open('mw_only_classyfire.pkl', 'rb') as f:
    mw_only_classyfire = pickle.load(f)

with open('mlmw_inchikey_classyfire.pkl', 'rb') as f:
    mlmwinchikeys_classyfire = pickle.load(f)

# all_super_class = set(ml_inchikey_classyfire['super_class']) | set(mw_inchikey_classyfire['super_class'])
all_super_class = set(mlmwinchikeys_classyfire['super_class'])
palette = itertools.cycle(qualitative.Set3)

color_map = {val: color for val, color in zip(all_super_class, palette)}

fig_ml = px.sunburst(ml_inchikey_classyfire, path=['kingdom', 'super_class', 'class'], values=None, color='super_class', color_discrete_map=color_map)
fig_ml.write_image("ml_classyfire.png")
fig_mw = px.sunburst(mw_inchikey_classyfire, path=['kingdom', 'super_class', 'class'], values=None, color='super_class', color_discrete_map=color_map)
fig_mw.write_image("mw_classyfire.png")
fig_intersection = px.sunburst(intersection_classyfire, path=['kingdom', 'super_class', 'class'], values=None, color='super_class', color_discrete_map=color_map)
fig_intersection.write_image("intersection_classyfire.png")
fig_mlonly = px.sunburst(ml_only_classyfire, path=['kingdom', 'super_class', 'class'], values=None, color='super_class', color_discrete_map=color_map)
fig_mlonly.write_image("mlonly_classyfire.png")
fig_mwonly = px.sunburst(mw_only_classyfire, path=['kingdom', 'super_class', 'class'], values=None, color='super_class', color_discrete_map=color_map)
fig_mwonly.write_image("mwonly_classyfire.png")
fig_mlmw = px.sunburst(mlmwinchikeys_classyfire, path=['kingdom', 'super_class', 'class'], values=None, color='super_class', color_discrete_map=color_map)
fig_mlmw.write_image("mlmw_classyfire.png")
