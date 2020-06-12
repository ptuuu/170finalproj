# STATS170AB Final Project Report By Yajie Zhang and You Li

The cleaned final data is stored as /demo/raw_data/datawithcor.csv.

## Demo Folder:
- The Demo file is saved as playground.ipynb, just hit the button "Run All Codes" and let it run and plot.
- Prerequisite for running the demo palette:
	- Pickle(pip install pickle) for loading our pre_trained data.
	- SKLearn(pip install sklearn) for evaluating metrics and splitting datas.
	- XGBoost(pip install XGBoost) for running our data.

- Some Restrictions on Demo:
	- In order to meet 1-minute maximum runtime, we used a subsample of 400 entries when training models. XGBoost will be significantly underfitted given a scenario like this, and the outcome is far away from the true outcome.
	- The keywords we extracted might be really poor in granularity since we only used around 3 % of the corpus, and our TF-IDF algorithm just barely converges, giving some unmeaningful outcomes for here.

- Interesting Features on Demo:
 	- You can track the trained Syntax Bank in the /demo/base_data file. 
 	- You can load the stopwords at /demo/base_data/stopword.dta
 	- Our Model is stored as 'pima.pickle.dat'
 	- The Encoded X Model for training is stored as 'all_feature.dat'

## Engineering Folder:
- As we included a large syntax base and file base locally, we will only upload notebooks we used for data cleaning and operating.
- We promised not to spread and leak the header file for our anti-anti-scraping Web Crawler, therefore, the web scraper will not be included for here.
- Cleaned_Big corresponds for the larger table and its cleaning.
- Cleaned_Small corresponds for the smaller table and its cleaning process. 
- We tested our ideas and code snippets in playground.ipynb.
- We write some helper functions in pyutil.py.
- 'STATS170B-Plot.ipynb' carries all the EDA results. 
- test.ipynb was our model training module. You can find compiled code snippets there.