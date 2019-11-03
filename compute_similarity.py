import pandas as pd
from rake_nltk import Rake
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


def run():
  data = pd.read_csv('data/recipes.csv', encoding = 'utf-8')
  # We're not gonna be using those
  data.drop(columns = ['Link', 'Image'], inplace = True)
  data.fillna('', inplace=True)
  print(data.shape)
  
  # Firstly, get the keywords from the longest texts
  data['About_Keywords'] = ""
  data['HowTo_Keywords'] = ""
  
  for i, row in data.iterrows():
    about = row['About']
    howto = row['HowToMake']
	
    # Rake removes English stopwords and punctuation, returns keywords
    r = Rake()
    r.extract_keywords_from_text(about)
	# Returns dictionary containing keywords and their scores
    about_keywords_dict = r.get_word_degrees()
	# Get only the keywords
    row['About_Keywords'] = list (about_keywords_dict.keys())
	# Same for How To Make
    r.extract_keywords_from_text(howto)
    howto_keyword_dict = r.get_word_degrees()
    row['HowTo_Keywords'] = list (howto_keyword_dict.keys())
	
  # These are now also not needed
  data.drop(columns = ['About', 'HowToMake'], inplace = True)
  print(data.head())

if __name__ == "__main__":
  run()