from lib import text_summary, get_sentiment
import csv
import json




origin = '/Users/assadnawaz/Documents/Thesis_data/aylien_covid_news_data.jsonl'
fName = "./T_13335.csv"

def read_file(file_name):
  limit = 13000 

  pointer = None
  pointer = open(fName, mode="w")
  file_pointer = csv.writer(pointer, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  with open(file_name) as fp:
    lines = file_pointer.readlines()
    for i, line in enumerate(lines):

      if i == limit:
        break
        
      jsonData = json.loads(line)
      try:
        text = text_summary(jsonData)
        sentiment = get_sentiment(jsonData)
        if len(text) == 0:
          continue
      except:
        continue

      file_pointer.writerow([text, sentiment])






read_file(origin)
