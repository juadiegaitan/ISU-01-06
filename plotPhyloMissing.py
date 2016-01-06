# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
data = pd.read_csv('sb32340_counts')
myplot = data.plot(kind='bar', legend=False)
plt.savefig('sb32340_counts.png', bbox_inches='tight', dpi=300)
