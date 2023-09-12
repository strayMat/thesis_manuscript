# %%
# The data is from the file retex.cvs, please plot me with matplotlib a timeline
# chart plot with vertical line for the labels:

from pathlib import Path
import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime


# %%
data = pd.read_csv('retex.csv')
col_date = "date"
col_label = "label"
data[col_date] = pd.to_datetime(data[col_date], format='%Y-%m-%d')
data.head()

# %%
# levels = np.tile(
#     [2, 1, -1, -2, -1],
#     int(np.ceil(len(data[col_date].dropna()) / 4)),
# )[: len(data[col_date].dropna())]
levels = [1, 2, -1, -2, 1, -1, 2, 1,  -2, -1, 2, 1, -1, -2, -1, 2]
# levels_down = np.tile(
#     [-5, -4, -3, -2, -1],
#     int(np.ceil(len(data[col_date].dropna()) / 5)),
# )[: len(data[col_date].dropna())]

fig, ax = plt.subplots(figsize=(8, 5), constrained_layout=True)

color ="darkslateblue"
ax.vlines(
    data[col_date], 0, levels, color=color
)  # The vertical stems.
ax.plot(
    data[col_date],
    np.zeros_like(data[col_date]),
    "-o",
    color="k",
    markerfacecolor="w",
)  # Baseline and markers on it.

for d, l, r in zip(
    data[col_date],
    levels,
    data[col_label],
):
    r = re.sub("#", "\n", r)
    #print(r)
    rotation = 0 if l < 0 else 0
    xtext = -2 if l < 0 else 0
    horizontalalignment = "center" if l < 0 else "center"
    ax.annotate(
        r,
        xy=(d, l),
        xytext=(xtext, np.sign(l) * 3),
        textcoords="offset points",
        horizontalalignment=horizontalalignment,
        verticalalignment="bottom" if l > 0 else "top",
        rotation=rotation,
        fontsize=13,
        wrap=True
    )

# format xaxis with 4 month intervals
#ax.set_xlim(datetime(2020, 1, 1), datetime(2023, 8, 1))
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
ax.yaxis.set_visible(False)
ax.spines[["left", "top", "right"]].set_visible(False)
ax.margins(y=0.1)
dir2img = Path("../img/")
plt.savefig(dir2img/"retex.png")
plt.savefig(dir2img/"retex.pdf")

# %%