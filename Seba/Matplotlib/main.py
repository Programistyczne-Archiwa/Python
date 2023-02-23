import matplotlib.pyplot as plt
import math
import numpy as np
import json

# Get data from json
with open('Matplotlib\data.json') as f:
    data = json.load(f)

# Make bar graph using data
bars = []
for i in data.keys():
    bars.append(i)

values = []
for i in data.values():
    values.append(i)

plt.bar(bars, values, color='green')
plt.show()