# 과제 5
# 3
import numpy as np
import pandas as pd

# 4
data = pd.read_csv('C:/data/president_heights.csv')

# 5
print(data.head())

# 6
heights = np.array(data['height(cm)'])
print(heights)

# 7
print("Mean height =", np.mean(heights))
print("Standard deviation =", np.std(heights))
print("Minimum height =", np.min(heights))
print("Maximum height =", np.max(heights))
print("25th percentile =", np.percentile(heights, 25))
print("Median =", np.median(heights))
print("75th percentile =", np.percentile(heights, 75))

# 8
max_idx = np.argmax(heights)
min_idx = np.argmin(heights)

print("Max_idx =", max_idx)
print("Min_idx =", min_idx)

# 9
max_name = data.iloc[max_idx]['name']
min_name = data.iloc[min_idx]['name']

print("The tallest president is", max_name)
print("The smallest president is", min_name)

# 10
from matplotlib import pyplot as plt
import seaborn

# 11
seaborn.set()

plt.hist(heights)
plt.title('Height Distribution of US President')
plt.xlabel('height (cm)')
plt.ylabel('number')
plt.show()