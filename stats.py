import pandas as pd
import sys
from collections import defaultdict
import matplotlib.pyplot as plt

def get_stats(stat='BaseSpirit'):
  data = pd.read_csv('data/recipes.csv')
  data.fillna('nothing', inplace=True)
  #  desired_cols = ['Glass','Occasions','Flavor','BaseSpirit','CocktailType','Preparation','Served','Strength','Difficulty','Hours','Theme','Brands','Garnish']
  stats = defaultdict(int)
  
  for i, row in data.iterrows():
    for col in data.columns:
      if col == stat:
        names = row[col].split(";")
        for name in names:
          if name not in stats:
            stats[name] = 1
          else:
            stats[name] += 1
	    
  for i in sorted(stats, key = stats.get, reverse = True):
    print(i + ": " + str(stats[i]))
  print("Missing:" + str(stats['nothing']))
  
  plt.barh(*zip(*stats.items()))
  plt.show()
		
if __name__ == "__main__":
  if len(sys.argv) > 1:
    get_stats(sys.argv[1])
  else:
    get_stats()