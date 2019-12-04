import pandas as pd
import numpy as np

def Run():
  data = pd.read_csv('data/recipes_crude.csv', encoding = 'utf-8')

  data.fillna('', inplace=True)
  print(data.shape)
  
  #  Remove Tacos
  data = data[~data.Name.str.contains('Taco')]
  print(data.shape)
   
  # Remove cocktails missing About or How to Make, as that screws recommendations and it's only a few of them (about 80)
  data['About'].replace('', np.nan, inplace = True)
  data['HowToMake'].replace('', np.nan, inplace = True)
  data.dropna(subset = ['About'], inplace = True)
  data.dropna(subset = ['HowToMake'], inplace = True)
  print(data.shape)
  
  data.to_csv('data/recipes.csv', index = False, encoding="utf-8")
  
  print(data.head())

if __name__ == "__main__":
  Run()