import pandas as pd
from rake_nltk import Rake
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


def run():
  data = pd.read_csv('data/recipes.csv', encoding = 'utf-8')
  # We're not gonna be using those
  data.drop(columns = ['Link', 'Image'], inplace = True)
  print(data.shape)
  print(data.head())

if __name__ == "__main__":
  run()