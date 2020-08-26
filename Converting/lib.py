import nltk
import inflect
import contractions
from bs4 import BeautifulSoup
from sklearn.preprocessing import LabelEncoder
from nltk.corpus import stopwords
from nltk import word_tokenize, sent_tokenize
from nltk.stem import LancasterStemmer, WordNetLemmatizer
import re, string, unicodedata


# To remove html tags if available
def remove_html_tags(text):
    
    soup = BeautifulSoup(text, "html.parser")
    text = soup.get_text()
    text = contractions.fix(text)
    return text

def text_clean(text):
  
  return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())


def remove_whiteSpace(text):
  text = text.replace("\n", "").replace("\t", "").replace('\\"',"")
  text = text.replace(',', "").replace('"', "")
  text = re.sub(' +', ' ', text)
  return text


def polished(text):
  text = remove_whiteSpace(text)
  text = remove_html_tags(text)
  text = text_clean(text)
  return text

def text_summary(j_data):
  text = ""
  for sentence in j_data['summary']['sentences']:
    text = text + ". "+ sentence
    text = polished(text)


  return text

def get_sentiment(j_data):
  polarity = j_data['sentiment']['body']['polarity']
  if polarity == 'positive':
      polarity = 1 
  else:
     polarity = 0 

  return polarity
