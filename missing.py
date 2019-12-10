import recommend

cat = [x for x in range(0,2213)]
about = [x for x in range(0,2213)]
comb = [x for x in range(0,2213)]
cat_boost = [x for x in range(0,2213)]
comb_boost = [x for x in range(0,2213)]

for i in range (0,2213):
  result = recommend.Recommend([i], 10, eval_test = True)
  cat = list(set(cat) - set(result[0]))
  about = list(set(about) - set(result[1]))
  comb = list(set(comb) - set(result[2]))
  cat_boost = list(set(cat_boost) - set(result[3]))
  comb_boost = list(set(comb_boost) - set(result[4]))
  
print(cat)
print(about)
print(comb)
print(cat_boost)
print(comb_boost)