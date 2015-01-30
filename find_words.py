import sys
import re
import urllib2

online_file = 'https://github.com/guru-beach/words/raw/master/word_list'
infile = 'word_list'
max_length = 10

def download_words():
  # Downloads a script friendly version of the word list
  global infile
  response = urllib2.urlopen(online_file)
  with open(infile, 'w') as OF:
    OF.write(response.read())
  
def check_file(infile):
  # See if the file exists locally and creates if it's not
  try:
    with open(infile, 'r') as IF:
      pass
  except IOError:
    download_words()

def create_regex(instring):
  # Creates a list of regexes to look for to be used in looking for exact matches
  char_dict = {}
  regex_list = []
  for c in instring:
    try:
      char_dict[c] += 1
    except:
      char_dict[c] = 1
  for ch, mult in char_dict.items():
    regex = ".*" + ("{}.*".format(ch) * mult)
    regex_list.append(re.compile(regex))
  return regex_list

def is_match(line, instring):
  # Looks for loose matches that will have at least one of each character in the input string
  for letter in instring:
    if letter not in line:
        return False
  return True

def is_good_match(line, regex_list):
  # Looks for exact matches of patterns based on multiples of same letters
  for regex in regex_list:
    try:
      regex.search(line).groups()
    except:
      return False
  return True

#print instring
def find_matches(instring, max_length):
  # Takes in a string, usually a WWF tile entry, and looks for possible matches
  # In an ENABLE dictionary file
  good_matches = []
  check_file(infile)
  regex_list = create_regex(instring)
  with open(infile, 'r') as wl:
    for line in wl:
      if (len(line) <= max_length):
        if is_match(line, instring):
          print line.strip()
        if is_good_match(line, regex_list):
          good_matches.append(line.strip())
  print "*** GOOD MATCHES ***"
  for match in good_matches:
    print match


if __name__ == '__main__':
  instring = sys.argv[1]
  try:
    max_length = int(sys.argv[2])
  except:
    pass
  find_matches(instring, max_length)
