import matplotlib.pyplot as plt
import seaborn as sns

tip = sns.load_dataset('tips')


sns.scatterplot('total_bill', 'tip', hue='sex', data=tip)

plt.show()