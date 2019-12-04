import pandas as pd
import numpy as np
import random
import sys

# So far only for a single name, to test the recommendations
def get_recommendation_list(profile_indices, count, similarity_file, eye_test = False, eval_test = False):
  # Load similarity matrices, possibly add switch to choose which one to use in the future
  similarity = np.load('data/' + similarity_file + '.npy')

  # Indices of titles
  indices = pd.read_csv('data/indices.csv')
  
  # Get the index of the drink given in 'name'
  # idx = indices.Name[indices.Name == "Gin Sonic"].index[0]
 
  scores = []
  
  # Get the sorted scores on the indices .. creating Series gives us the ability to pair drink with its score and retrieve it based on its index
  for i in range(0, len(profile_indices)):
    scores.append(pd.Series(similarity[profile_indices[i]]).sort_values(ascending = False))
	
  top_count = []
  
  # Get the top 'count'
  for i in range(0, len(profile_indices)):
    top_count += list(scores[i].iloc[1:31].index)
  
  recommended = []
	
  recommended = fill_recommendation_list(count, top_count, profile_indices)
	
  if eye_test:
    return recommended
	
  if eval_test:
    return top_count
	
  return [get_drinks(recommended)]

  
# Fill the resulting list with drinks randomly from selected top few  
def fill_recommendation_list(count, list, profile):
  recommended = []
  while len(recommended) < count:
    drink = random.choice(list) 
    if drink not in recommended and drink not in profile:
      recommended.append(drink)	
  return recommended
  
  
# Convert index into a cocktail name, for lists  
def get_names(idxs):
  names = []
  indices = pd.read_csv('data/indices.csv')
  for drink in idxs:
    names.append(indices.Name[drink])
  return names 

def get_drink(id, drinks_file):
  if drinks_file is None:
    drinks_file = pd.read_csv('data/recipes.csv')
  return drinks_file.iloc[id].to_json()

def get_drinks(indices):
  drinks_file = pd.read_csv('data/recipes.csv')
  drinks = []
  for index in indices:
    drinks.append(get_drink(index, drinks_file))
  return drinks

# Eye test for easier output of names to console
# Eval test for comparing categories vs about + howto
def Recommend(profile_indices, count, eye_test = False, eval_test = False):
  categories_list = get_recommendation_list(profile_indices, count, 'categories_similarity', eye_test, eval_test)
  about_howto_list = get_recommendation_list(profile_indices, count, 'about_howto_similarity', eye_test, eval_test)
  combined_list = get_recommendation_list(profile_indices, count, 'combined_similarity', eye_test, eval_test)
  
  categories_boosted_list = get_recommendation_list(profile_indices, count, 'categories_similarity_boosted', eye_test, eval_test)
  combined_boosted_list = get_recommendation_list(profile_indices, count, 'combined_similarity_boosted', eye_test, eval_test)
  
  return [categories_list, about_howto_list, combined_list, categories_boosted_list, combined_boosted_list]
  
  
if __name__ == "__main__":
  
  profile = [27,60,80,1563,1012,861,457,950]

  rec_list = Recommend(profile, 10, False, True);
  print("\nProfile: \n")
  print(get_names(profile))
  print("\n\nBased on Categories: \n")
  print(get_names(rec_list[0]))
  print("\n\nBased on About and How To: \n")
  print(get_names(rec_list[1]))
  print("\n\nBased on Both: \n")
  print(get_names(rec_list[2]))
  print("\n\nBased on Boosted Categories: \n")
  print(get_names(rec_list[3]))
  print("\n\nBased on Boosted Combined: \n")
  print(get_names(rec_list[4]))