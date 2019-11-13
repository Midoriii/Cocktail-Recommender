import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


def Run():
  data = pd.read_csv('data/recipes.csv', encoding = 'utf-8')
  # We're not gonna be using those
  data.drop(columns = ['Link', 'Image'], inplace = True)
  data.fillna(' ', inplace=True)
  print(data.shape)
  
  #  These two columns could benefit from lowercasing, other columns are well managed
  data['Glass'] = data['Glass'].str.lower()
  data['Garnish'] = data['Garnish'].str.lower()
  
  # Replace ';' separator by white space
  separated_cols = ['Ingredients','Garnish','Glass','Flavor','BaseSpirit','CocktailType','Preparation','Served','Difficulty','Hours','Occasions','Theme','Brands']
  
  for i, row in data.iterrows():
    for col in data.columns:
      if col in separated_cols:
        row[col] = row[col].replace(';',' ')
  
  # Create three bags of words - one from just the categories, one from About and How To Make (possibly reduce to just About) and final one from eveything
  data['bag_of_words_categories'] = ""
  data['bag_of_words_about_howto'] = ""
  data['bag_of_words_combined'] = ""
  
  # Concat all strings together into bags of words before tf-idf vectorization (which also tokenizes)
  for i, row in data.iterrows():
    for col in data.columns:
      if col in ['About','HowToMake']:
        row['bag_of_words_about_howto'] += row[col] + " "
      if col not in ['About','HowToMake','Name','bag_of_words_about_howto','bag_of_words_categories','bag_of_words_combined']:
        row['bag_of_words_categories'] += row[col] + " "

    row['bag_of_words_combined'] = row['bag_of_words_about_howto'] + " " + row['bag_of_words_categories']
  
  # We'll want indices bound to names .. because similarity matrix is just that, a matrix, and we don't want to load the whole recipes.csv and compute it again and again
  # in recommendation, so we need a way to bind the indices in matrices to cocktail names, to find the similarity scores of input drink AND get the names of found similar indices
  data['Name'].to_csv('data/indices.csv', header=['Name'], index = False)
  data.set_index('Name', inplace = True)
  
  # We won't need anything but the Names and bags now
  data.drop(columns = [col for col in data.columns if col not in ['Name','bag_of_words_categories','bag_of_words_about_howto','bag_of_words_combined']], inplace = True)
  
  # Create a vectorizer that does almost everything for us
  tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df = 0, stop_words='english')
  
  # Apply the vectorizer's magic on the bags of words
  categories_matrix = tf.fit_transform(data['bag_of_words_categories'])
  about_howto_matrix = tf.fit_transform(data['bag_of_words_about_howto'])
  combined_matrix = tf.fit_transform(data['bag_of_words_combined'])
  
  # Get the similarity matrices
  sim_categories = cosine_similarity(categories_matrix, categories_matrix)
  sim_about_howto = cosine_similarity(about_howto_matrix, about_howto_matrix)
  sim_combined = cosine_similarity(combined_matrix, combined_matrix)
  
  # Save the similarity matrices to be loaded by the recommender
  np.save('data/categories_similarity.npy', sim_categories)
  np.save('data/about_howto_similarity.npy', sim_about_howto)
  np.save('data/combined_similarity.npy', sim_combined)
  
  print(data.head())

if __name__ == "__main__":
  Run()