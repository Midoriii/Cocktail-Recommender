# Cocktail Recommender

A PV254 project. Description will be added

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
* Basic approach is to keep user's favourite drinks and then recommend a number of drinks similar to few randomly selected from the ones the customer likes. 
* Advanced approach would be to select several most important categories and encode user profile and drinks with one-hot encoding. Recommendation would then be based on the resulting score of matrix multiplication between those two.

## Evaluation

* 'Eye-test' on the suitability of the recommended cocktails, try to evaluate strengths and weaknesses of all approaches.
* Might ask a bartending friend for an expert opinion.
* If time permits, gather responses from a small group of testers

## Authors

* **Marek Kucera**
* **Štepán Beneš**
* **Lukáš Matta**

## License

ehhh

## Acknowledgments

* Hat tip to anyone whose code was used