Yelp-er
=======

To read about the project in short, please refer to slides.pdf. To understand the project in depth, please refer to report.pdf.

Heatmap
=======
There are 2 main files that you need to access for heatmap:

1) createLocation.py: this file reads input from 'yelp_academic_dataset_business.json' and convert it into locations (latitude+longitude) based on the categories of each business. 
2) main.html: Once locations are created (locations are present in the uploaded code), run main.html. This file takes category as input from user and generates heatmap on google map using google javascript api v3.



Gamification
============
createTags.py contains the entire gamification code. It reads the data from 'yelp_academic_dataset_user.json' and create tags for each user based on the following attributes of user:
a) review_count, b) yelping_since, c) compliments, d) fans, e) friends, and f) votes



Semantic Analysis
=================
We used mallet for this. Below are the commands that were used:

a) bin/mallet import-dir --input /home/naman/Downloads/yelp_dataset_challenge_academic_dataset/code/review/ --output topic-input.mallet --keep-sequence --remove-stopwords

b) bin/mallet train-topics --input topic-input.mallet --num-topics 15 --output-topic-keys topic-keys --word-topic-counts-file word-topic-counts --optimize-interval 10 --optimize-burn-in 20

On running this, you will have topics and strength of each word for their respective topics (can be multiple). You can fill in this information in wordle to get the word clouds.



Retail Group
