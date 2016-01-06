# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
data = pd.read_csv('counts')
data.plot(kind='bar', legend=False)
plt.savefig('hist1.svg', bbox_inches='tight', dpi=300)
plt.savefig('readCounts.png', bbox_inches='tight', dpi=300)
