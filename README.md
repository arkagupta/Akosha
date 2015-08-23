# Akosha
#### Task : “American Sniper”

###### Step 1 :
  Run the script Main.py.
  It will ask you to browse and select the corpus you want to train your model on.
  Once selected the corpus to train the model it will create 6 pickle objects and object components respectively.
###### Step 2 :
  Run the Model_Run.py file.
  It will ask to enter the Text and then use the same to predict next two words.

#### Requirements:
1. Python 2.7 or higher
2. Python Packages :
 * [**NLTK**](http://www.nltk.org/install.html)
 * [**Sklearn**](http://scikit-learn.org/stable/install.html)
 * [**Easygui**](https://pypi.python.org/pypi/easygui/0.97.2)
 * [**Regular Expression**](https://docs.python.org/2/library/re.html)
 * [**Pandas**](https://pypi.python.org/pypi/pandas/0.16.2/)

#### Approach:
Since the corpus provided is tweets so expecting a proper english sentence structure would be fuzzy.So POS tagging would not be a better match and also if we think of a generalizing perspective then the given corpus would be pretty biased and erroneous where we need more meaningfull sample.So in order to predict the next two words for the given corpus a reasonable approach(given the time constraint I had) according to me was N-gram probability.However I just attempted uptill 6 gram probability but a better approach could be going for the grams based on length of words sequentially provided.
###### So the logic is :
* At first check whether complete sentence or not
* 1 word given then use bigram and then take the two grams as input and run trigram for next word.
* 2 words given then use trigram and then take the three grams as input and run fourgram for next word.
* 3 words given then use fourgram and then take the four grams as input and run fivegram for next word.
* 4 words given then use fivegram and then take the five grams as input and run sixgram for next word.
* Anything greater than length 4 take only the last 4 words into consideration and do as is in 4 words approach.

