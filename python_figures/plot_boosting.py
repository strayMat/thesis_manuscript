# %%
"""
======================================
Decision Tree Regression with AdaBoost
======================================

A decision tree is boosted using the AdaBoost.R2 [1] algorithm on a 1D
sinusoidal dataset with a small amount of Gaussian noise.
299 boosts (300 decision trees) is compared with a single decision tree
regressor. As the number of boosts is increased the regressor can fit more
detail.

.. [1] H. Drucker, "Improving Regressors using Boosting Techniques", 1997.


Adapt the scikit-learn example to include on the same dataset, trees, random forest and boosting.
"""
print(__doc__)

# Author: Noel Dawe <noel.dawe@gmail.com>
#
# License: BSD 3 clause

# importing necessary libraries
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor, RandomForestRegressor

#plt.rcParams['text.color'] = 'w'
dir2figures = Path("../img/chapter_1/")

# Create the dataset
rng = np.random.RandomState(1)
X = np.linspace(0, 6, 100)[:, np.newaxis]
y = -np.sin(X).ravel() + np.sin(6 * X).ravel() + rng.normal(0, 0.1, X.shape[0])

# %%
# Tree
tree_1 = DecisionTreeRegressor(max_depth=1)
tree_2 = DecisionTreeRegressor(max_depth=2)
tree_3 = DecisionTreeRegressor(max_depth=5)

## Fit tree models
tree_1.fit(X, y)
tree_2.fit(X, y)
tree_3.fit(X, y)

## Predict
y_tree_1 = tree_1.predict(X)
y_tree_2= tree_2.predict(X)
y_tree_3= tree_3.predict(X)

plt.figure(figsize=(6.5, 3.25), edgecolor='w')
plt.axes([0, 0, 1, 1])
plt.scatter(X, y, c='k')
plt.plot(X, y_tree_1, label="Max depth=1", linewidth=2)
plt.axis('tight')
plt.axis('off')
plt.legend(loc='upper left', frameon=False)
plt.savefig(dir2figures/'tree_1.pdf', edegecolor='none', facecolor='none')
plt.plot(X, y_tree_2, label="Max depth=2", linewidth=2)
plt.legend(loc='upper left', frameon=False)
plt.savefig(dir2figures/'tree_2.pdf', edegecolor='none', facecolor='none')
plt.plot(X, y_tree_3, label="Max depth=5", linewidth=2)
plt.legend(loc='upper left', frameon=False)
plt.savefig(dir2figures/'tree_3.pdf', edegecolor='none', facecolor='none')
plt.close()

# %%
# Random Forest
forest_1 = DecisionTreeRegressor(max_depth=4)

forest_2 = RandomForestRegressor(max_depth=4, n_estimators=2, random_state=1)

forest_3 = RandomForestRegressor(max_depth=4, n_estimators=4, random_state=1)

forest_4 = RandomForestRegressor(max_depth=4, n_estimators=300, random_state=1)

forest_1.fit(X, y)
forest_2.fit(X, y)
forest_3.fit(X, y)
forest_4.fit(X, y)

# Predict
y_forest_1 = forest_1.predict(X)
y_forest_2 = forest_2.predict(X)
y_forest_3 = forest_3.predict(X)
y_forest_4 = forest_4.predict(X)

# Plot the results
plt.figure(figsize=(6.5, 3.25), edgecolor='w')
plt.axes([0, 0, 1, 1])
plt.scatter(X, y, c='k')
plt.plot(X, y_forest_1, label="1 Tree", linewidth=2)
plt.axis('tight')
plt.axis('off')
plt.legend(loc='upper left', frameon=False)
plt.savefig(dir2figures/'forest_1.pdf', edegecolor='none', facecolor='none')
plt.plot(X, y_forest_2, label="2 Trees combined", linewidth=2)
plt.legend(loc='upper left', frameon=False)
plt.savefig(dir2figures/'forest_2.pdf', edegecolor='none', facecolor='none')
plt.plot(X, y_forest_3, label="3 Trees combined", linewidth=2)
plt.legend(loc='upper left', frameon=False)
plt.savefig(dir2figures/'forest_3.pdf', edegecolor='none', facecolor='none')
plt.plot(X, y_forest_4, label="300 Trees combined", linewidth=2)
plt.legend(loc='upper left', frameon=False)
plt.savefig(dir2figures/'forest_4.pdf', edegecolor='none', facecolor='none')
plt.show()
plt.close()

# %% 
# Boosting 
## Fit regression model
clf_1 = DecisionTreeRegressor(max_depth=4)

clf_2 = AdaBoostRegressor(DecisionTreeRegressor(max_depth=4),
                          n_estimators=2, random_state=1)

clf_3 = AdaBoostRegressor(DecisionTreeRegressor(max_depth=4),
                          n_estimators=4, random_state=1)

clf_4 = AdaBoostRegressor(DecisionTreeRegressor(max_depth=4),
                          n_estimators=300, random_state=1)

clf_1.fit(X, y)
clf_2.fit(X, y)
clf_3.fit(X, y)
clf_4.fit(X, y)

# Predict
y_1 = clf_1.predict(X)
y_2 = clf_2.predict(X)
y_3 = clf_3.predict(X)
y_4 = clf_4.predict(X)

# Plot the results
plt.figure(figsize=(6.5, 3.25), edgecolor='w')
plt.axes([0, 0, 1, 1])
plt.scatter(X, y, c='k')
plt.plot(X, y_1, label="1 Tree", linewidth=2)
plt.axis('tight')
plt.axis('off')
plt.legend(loc='upper left', frameon=False)
plt.savefig(dir2figures/'boosting_1.pdf', edegecolor='none', facecolor='none')
plt.plot(X, y_2, label="2 Trees combined", linewidth=2)
plt.legend(loc='upper left', frameon=False)
plt.savefig(dir2figures/'boosting_2.pdf', edegecolor='none', facecolor='none')
plt.plot(X, y_3, label="3 Trees combined", linewidth=2)
plt.legend(loc='upper left', frameon=False)
plt.savefig(dir2figures/'boosting_3.pdf', edegecolor='none', facecolor='none')
plt.plot(X, y_4, label="300 Trees combined", linewidth=2)
plt.legend(loc='upper left', frameon=False)
plt.savefig(dir2figures/'boosting_4.pdf', edegecolor='none', facecolor='none')

plt.show()

