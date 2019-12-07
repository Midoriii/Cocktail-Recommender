import recommend
import matplotlib.pyplot as plt
import numpy as np


def Run():
  scores = [[0 for x in range(6)] for x in range(2213)] 
  # Hardcoded because whatever 2213
  for i in range(0,2213):
    lists = recommend.Recommend([i], 10, eval_test = True)
	
    categories_vs_about_howto = list(set(lists[0] + lists[1]))
    categories_vs_boosted_categories = list(set(lists[0] + lists[3]))
    combined_vs_boosted_combined = list(set(lists[2] + lists[4]))
    categories_boosted_vs_about_howto = list(set(lists[3] + lists[1]))
    categories_vs_combined = list(set(lists[0] + lists[2]))
    categories_boosted_vs_combined_boosted = list(set(lists[3] + lists[4]))
    
    for j in range(0, len(categories_vs_about_howto)):
      if categories_vs_about_howto[j] in lists[0] and categories_vs_about_howto[j] in lists[1]:
        scores[i][0] += 1		
    for j in range(0, len(categories_vs_boosted_categories)):
      if categories_vs_boosted_categories[j] in lists[0] and categories_vs_boosted_categories[j] in lists[3]:
        scores[i][1] += 1
    for j in range(0, len(combined_vs_boosted_combined)):
      if combined_vs_boosted_combined[j] in lists[2] and combined_vs_boosted_combined[j] in lists[4]:
        scores[i][2] += 1
    for j in range(0, len(categories_boosted_vs_about_howto)):
      if categories_boosted_vs_about_howto[j] in lists[3] and categories_boosted_vs_about_howto[j] in lists[1]:
        scores[i][3] += 1
    for j in range(0, len(categories_vs_combined)):
      if categories_vs_combined[j] in lists[0] and categories_vs_combined[j] in lists[2]:
        scores[i][4] += 1
    for j in range(0, len(categories_boosted_vs_combined_boosted)):
      if categories_boosted_vs_combined_boosted[j] in lists[3] and categories_boosted_vs_combined_boosted[j] in lists[4]:
        scores[i][5] += 1
  
  scores = np.array(scores)
  #print(scores)
  plt.hist(scores[:,0], bins=31, color='blue', rwidth=0.99)
  plt.xlim(0,30)
  plt.title('Categories vs About & How To Make')
  plt.xlabel('Intersection #')
  plt.ylabel('Count')
  plt.savefig('graphs/graph1_30.png')
  plt.clf()  
  
  plt.hist(scores[:,1], bins=31, color='blue', rwidth=0.99)
  plt.xlim(0,30)
  plt.title('Categories vs Boosted Categories')	
  plt.xlabel('Intersection #')
  plt.ylabel('Count')
  plt.savefig('graphs/graph2_30.png')
  plt.clf()  
  
  plt.hist(scores[:,2], bins=31, color='blue', rwidth=0.99)
  plt.xlim(0,30)
  plt.title('Combined vs Boosted Combined')
  plt.xlabel('Intersection #')
  plt.ylabel('Count')
  plt.savefig('graphs/graph3_30.png')
  plt.clf()  
  
  plt.hist(scores[:,3], bins=31, color='blue', rwidth=0.99)
  plt.xlim(0,30)
  plt.title('Boosted Categories vs About & How To Make')	
  plt.xlabel('Intersection #')
  plt.ylabel('Count')
  plt.savefig('graphs/graph4_30.png')
  plt.clf() 
  
  plt.hist(scores[:,4], bins=31, color='blue', rwidth=0.99)
  plt.xlim(0,30)
  plt.title('Categories vs Combined')	
  plt.xlabel('Intersection #')
  plt.ylabel('Count')
  plt.savefig('graphs/graph5_30.png')
  plt.clf() 
  
  plt.hist(scores[:,5], bins=31, color='blue', rwidth=0.99)
  plt.xlim(0,30)
  plt.title('Boosted Categories vs Boosted Combined')	
  plt.xlabel('Intersection #')
  plt.ylabel('Count')
  plt.savefig('graphs/graph6_30.png')
		
if __name__ == "__main__":
  Run()