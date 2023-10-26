# %%
from pathlib import Path
import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import seaborn as sns


"""
Based on FDA database on approved devices with AI : https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-aiml-enabled-medical-devices

Good related reading : 
- https://magazine.amstat.org/blog/2023/09/01/medicaldevices/

Main findings: almost all in radiology, and surge in 2020-2021.
"""
# %%

data = pd.read_excel(
    "Artificial Intelligence and Machine Learning (AIML)-Enabled Medical Devices FDA.xlsx",
    skiprows=1,
)
col_date = "Date of Final Decision"
col_category = "Specialty"
data[col_date] = pd.to_datetime(data[col_date], format="%m/%d/%Y")
data["Year"] = data[col_date].dt.year
data = data.rename(columns={"Panel (Lead)": col_category})
data.head()

# %%
label = "Number of FDA approved devices with AI"
count_by_month_category = (
    data.groupby(["Year", col_category])["Device"]
    .count()
    .reset_index()
    .rename(columns={"Device": label})
)


specialty_counts = (
    count_by_month_category.groupby(col_category)[label]
    .sum()
    .sort_values(ascending=False)
)
specialty_sup_5_names = specialty_counts[specialty_counts >= 5].index
# %%
final_year = 2022
first_year = 2008

data_to_plot = count_by_month_category.loc[
    (count_by_month_category[col_category].isin(specialty_sup_5_names))
    & (count_by_month_category["Year"] <= final_year)
]

fig, ax = plt.subplots(figsize=(5, 4), constrained_layout=True)

sns.lineplot(
    ax=ax,
    data=data_to_plot,
    x="Year",
    y=label,
    hue=col_category,
    hue_order=specialty_sup_5_names,
)

ax.set_xlim((first_year, final_year + 1))
ax.set_xticks(np.arange(first_year, final_year + 1).astype(int), minor=True)

path2fig = Path("../img/fda_devices")
plt.savefig(f"{str(path2fig)}.png", bbox_inches="tight", dpi=300)
plt.savefig(f"{str(path2fig)}.pdf", bbox_inches="tight")
