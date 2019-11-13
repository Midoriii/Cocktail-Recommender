import pandas as pd
import numpy as np
import sys

# So far only for a single name, to test the recommendations
def Recommend(name, count):
  # Load similarity matrices, possibly add switch to choose which one to use in the future
  sim_categories = np.load('data/categories_similarity.npy')
  sim_about_howto = np.load('data/about_howto_similarity.npy')
  sim_combined = np.load('data/combined_similarity.npy')
  
  # Indices of titles
  indices = pd.read_csv('data/indices.csv')
  
  # Get the index of the drink given in 'name'
  idx = indices.Name[indices.Name == name].index[0]
  
  # Get the sorted scores on the index idx .. creating Series gives us the ability to pair drink with its score and retrieve it based on its index
  scores_categories = pd.Series(sim_categories[idx]).sort_values(ascending = False)
  scores_about_howto = pd.Series(sim_about_howto[idx]).sort_values(ascending = False)
  scores_combined = pd.Series(sim_combined[idx]).sort_values(ascending = False)
  
  # Get the top 'count'
  top_count_categories = list(scores_categories.iloc[1:count+1].index)
  top_count_about_howto = list(scores_about_howto.iloc[1:count+1].index)
  top_count_combined = list(scores_combined.iloc[1:count+1].index)
  
  recommended_categories = []
  recommended_about_howto = []
  recommended_combined = []
  
  # Get the names from indices
  for drink in top_count_categories:
    recommended_categories.append(indices.Name[drink])
  for drink in top_count_about_howto:
    recommended_about_howto.append(indices.Name[drink])
  for drink in top_count_combined:
    recommended_combined.append(indices.Name[drink])
	
  return [recommended_categories, recommended_about_howto, recommended_combined]

if __name__ == "__main__":
  list = Recommend("Night Flights", 10);
  print("\n\nBased on Categories: \n")
  print(list[0])
  print("\n\nBased on About and How To: \n")
  print(list[1])
  print("\n\nBased on Both: \n")
  print(list[2])