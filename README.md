# Cocktail Recommender

A PV254 project. A Content-based cocktail recommender, works by first building a user profile of drinks and then recommends additional cocktails based on user's liking.
Yo can find working application here: http://drinks.mattadev.eu/

## Requirements

* stored in **requirements.txt**
* generate current with **pipreqs . --encoding=utf-8 --force**

## Business Case

* Could be used on a Liquor selling website. Customer builds his favourite drink portfolio and might buy merchandise based on cocktails recommended to him. Alcohol connoisseurs might enjoy exploring new drinks and mixing them on their own.

## Data

* More than 2300 drink recipes from <a href="https://www.liquor.com/recipes">this page</a>. 
* 14 Categories + Description + How to make
* Some categories not always filled
* Usually several values dominate single category (i.e. Base Spirits) with counts >100.

## Algorithms

* Scrapped data is passed through an tf-idf vectorizer and cosine similarity between the tf-idf-scores is computed and stored.
* tf-idf is done on words in: 1) Categories without About and How to make  2) Just About and How to make  3) Both combined
* Basic approach is to keep user's favourite drinks, get the top 30 similar drinks to each of user's already liked drinks and from those randomly select desired number for the final suggestion. 
* In addition we've also artificially boosted the importance of some categories in two additional tf-idfs.

## Evaluation

* 'Eye-test' on the suitability of the recommended cocktails.
* Evaluator consists of randomly chosen drink and 5 rows of 3 recommendations, each row is one randomly shuffled method of the five mentioned.
* Chosen row gains a point for its method
* Combined approach won this evaluation, with methods based on categories not too far behind, even the boosted variants. Method based on pure description fell short.

* Similarity between two methods is found by using intersection on the sets of drinks they recommend. 
* Categories make up a significiant portion of Combined list, with few important drinks recommended by About and How to make filling the rest.

## Authors

* **Marek Kucera**
* **Štepán Beneš**
* **Lukáš Matta**

## License

ehhh

## Acknowledgments

* Hat tip to anyone whose code was used
