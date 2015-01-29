import sys
import urllib2

online_file = 'https://github.com/guru-beach/words/raw/master/word_list'
infile = 'word_list'
max_length = 10

def is_match(line, instring):
  for letter in instring:
    if letter not in line:
        return False
  return True

def download_words():
  global infile
  response = urllib2.urlopen(online_file)
  with open(infile, 'w') as OF:
    OF.write(response.read())
  
def check_file(infile):
  try:
    with open(infile, 'r') as IF:
      pass
  except IOError:
    download_words()

#print instring
def find_matches(instring, max_length):
  check_file(infile)
  with open(infile, 'r') as wl:
   for line in wl:
    if is_match(line, instring):
     if (len(line) <= max_length):
       print line.strip()

if __name__ == '__main__':
  instring = sys.argv[1]
  try:
    max_length = int(sys.argv[2])
  except:
    pass
  find_matches(instring, max_length)
