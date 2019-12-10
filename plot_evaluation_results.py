import matplotlib.pyplot as plt
import numpy as np

values = [33, 10, 62, 27, 31]
methods = ('Profile','Description','Combined','Profile_B','Combined_B')


plt.figure(figsize=(8,7))
y_pos = np.arange(len(methods))
plt.bar(y_pos, values, color='orange')

plt.xticks(y_pos, methods, rotation=25, fontsize='12', horizontalalignment='right')

plt.title('Evaluation results')
plt.ylabel('Times chosen as the best')
plt.savefig('graphs/eval_results.png')