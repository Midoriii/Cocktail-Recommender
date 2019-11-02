import pandas as pd
from rake_nltk import Rake
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

def run():
  data = pd.read_csv('data/recipes.csv', encoding = 'utf-8')
  data = data[['Name','About','HowToMake','Ingredients','Garnish','Glass','Flavor','BaseSpirit','CocktailType','Preparation','Served','Strength','Difficulty','Hours','Occasions','Theme','Brands']]
  print(data.shape)
  print(data.head())

if __name__ == "__main__":
  run()