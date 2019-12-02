import pandas as pd
import numpy as np
import random
import sys

# So far only for a single name, to test the recommendations
def Recommend(profile_indices, count):
  # Load similarity matrices, possibly add switch to choose which one to use in the future
  sim_categories = np.load('data/categories_similarity.npy')
  sim_about_howto = np.load('data/about_howto_similarity.npy')
  sim_combined = np.load('data/combined_similarity.npy')
  
  # Indices of titles
  indices = pd.read_csv('data/indices.csv')
  
  # Get the index of the drink given in 'name'
  # idx = indices.Name[indices.Name == "Gin Sonic"].index[0]
 
  scores_categories = []
  scores_about_howto = []
  scores_combined = []
  
  # Get the sorted scores on the indices .. creating Series gives us the ability to pair drink with its score and retrieve it based on its index
  for i in range(0, len(profile_indices)):
    scores_categories.append(pd.Series(sim_categories[profile_indices[i]]).sort_values(ascending = False))
    scores_about_howto.append(pd.Series(sim_about_howto[profile_indices[i]]).sort_values(ascending = False))
    scores_combined.append(pd.Series(sim_combined[profile_indices[i]]).sort_values(ascending = False))
	
  top_count_categories = []
  top_count_about_howto = []
  top_count_combined = []
  
  # Get the top 'count'
  for i in range(0, len(profile_indices)):
    top_count_categories += list(scores_categories[i].iloc[1:51].index)
    top_count_about_howto += list(scores_about_howto[i].iloc[1:51].index)
    top_count_combined += list(scores_combined[i].iloc[1:51].index)
  
  recommended_categories = []
  recommended_about_howto = []
  recommended_combined = []
  
  # Get the names from indices
  # This will be just debug info, since we only want to pass indices around, because of duplicate names !!!
  #for drink in top_count_categories:
  #  recommended_categories.append(indices.Name[drink])
  #for drink in top_count_about_howto:
  #  recommended_about_howto.append(indices.Name[drink])
  #for drink in top_count_combined:
  #  recommended_combined.append(indices.Name[drink])
	
  recommended_categories = fill_recommendation_list(count, top_count_categories, profile_indices)
  recommended_about_howto = fill_recommendation_list(count, top_count_about_howto, profile_indices)
  recommended_combined = fill_recommendation_list(count, top_count_combined, profile_indices)
	
  return [recommended_categories, recommended_about_howto, recommended_combined]

  
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
  
  
  
if __name__ == "__main__":
  
  profile = [27,60,80,1576,1025,860,457,962]

  rec_list = Recommend(profile, 10);
  print("\nProfile: \n")
  print(get_names(profile))
  print("\n\nBased on Categories: \n")
  print(get_names(rec_list[0]))
  print("\n\nBased on About and How To: \n")
  print(get_names(rec_list[1]))
  print("\n\nBased on Both: \n")
  print(get_names(rec_list[2]))