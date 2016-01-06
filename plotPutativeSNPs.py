# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
data = pd.read_csv('putativeSNPs')
myplot = data.plot(kind='bar', legend=False)
plt.savefig('putativeSNPcounts.png', bbox_inches='tight', dpi=300)
