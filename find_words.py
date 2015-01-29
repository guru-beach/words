import sys

infile = 'word_list'
instring = sys.argv[1]
max_length = 10
try:
  max_length = int(sys.argv[2])
except:
  pass

#print sys.argv
#print instring
#print max_length

def is_match(line, instring):
  for letter in instring:
    if letter not in line:
        return False
  return True
 
#print instring
with open(infile, 'r') as wl:
  for line in wl:
   if is_match(line, instring):
    if (len(line) <= max_length):
      #print len(line) <= max_length
      #print "{}: {}, {}".format(line, len(line), max_length)
      print line.strip()
