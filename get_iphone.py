import urllib2
import sys

find_words_online = 'https://raw.githubusercontent.com/guru-beach/words/master/find_words.py'
find_words = "find_words.py"

response = urllib2.urlopen(find_words_online)
with open(find_words, 'w') as OF:
  OF.write(response.read())
