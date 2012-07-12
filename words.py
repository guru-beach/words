#Initialized the tiles in a dictionary
#Player 0, player 1
#On each move
#Input the tiles played and the score received (optional)

import time
import string
import pickle
#initial_tiles { letter, [count, score]}
initial_tiles = {'a': [ 9, 1 ],
                'b': [ 2, 4 ],
                'c': [ 2, 4 ],
                'd': [ 5, 2 ],
                'e': [ 13, 1 ],
                'f': [ 2, 4 ],
                'g': [ 3, 3 ],
                'h': [ 4, 3 ],
                'i': [ 8, 1 ],
                'j': [ 1, 10 ],
                'k': [ 1, 5 ],
                'l': [ 4, 2 ],
                'm': [ 2, 4 ],
                'n': [ 5, 2 ],
                'o': [ 8, 1 ],
                'p': [ 2, 4 ],
                'q': [ 1, 10 ],
                'r': [ 6, 1 ],
                's': [ 5, 1 ],
                't': [ 7, 1 ],
                'u': [ 4, 2 ],
                'v': [ 2, 5 ],
                'w': [ 2, 4 ],
                'x': [ 1, 8 ],
                'y': [ 2, 3 ],
                'z': [ 1, 10 ],
                '-': [ 2, 10 ]
               }
def init_tiles():
  initial_tiles = {'a': [ 9, 1 ],
                   'b': [ 2, 4 ],
                   'c': [ 2, 4 ],
                   'd': [ 5, 2 ],
                   'e': [ 13, 1 ],
                   'f': [ 2, 4 ],
                   'g': [ 3, 3 ],
                   'h': [ 4, 3 ],
                   'i': [ 8, 1 ],
                   'j': [ 1, 10 ],
                   'k': [ 1, 5 ],
                   'l': [ 4, 2 ],
                   'm': [ 2, 4 ],
                   'n': [ 5, 2 ],
                   'o': [ 8, 1 ],
                   'p': [ 2, 4 ],
                   'q': [ 1, 10 ],
                   'r': [ 6, 1 ],
                   's': [ 5, 1 ],
                   't': [ 7, 1 ],
                   'u': [ 4, 2 ],
                   'v': [ 2, 5 ],
                   'w': [ 2, 4 ],
                   'x': [ 1, 8 ],
                   'y': [ 2, 3 ],
                   'z': [ 1, 10 ],
                   '-': [ 2, 10 ]
                  }
  return initial_tiles

class wordsGame:
    
    def __init__(self, player):
      self.startTime = int(time.time())
      self.tiles = init_tiles()
      self.op = player
      self.play_dict = {'me': { 'tiles' : [], 'score' : 0},
                        'op': { 'tiles' : [], 'score' : 0}}

    def move(self, side, letters, score=0):
      for letter in letters:
        self.tiles[letter][0] -= 1
        self.play_dict[side]['tiles'].append(letter)
      self.play_dict[side]['score'] += score

    def remains(self):
      for lower in string.ascii_lowercase+'-':
        count = self.tiles[lower][0]
        if count:
          print "{}:{}".format(lower, count)

    def adjust(self, player, score):
      self.play_dict[player]['score'] = score

    def save(self):
      with open('{}.{}'.format(self.op, self.startTime), 'w') as outFile:
        pickle.dump(self, outFile)

    def __str__(self):
      outString = ""
      i = 0
      col = 7
      outString += "Tiles:"
      for letter in string.ascii_lowercase+'-':
        if not i % col:
          outString += "\n"
        count = self.tiles[letter][0]
        if count:
          outString += "{}:{}   ".format(letter, count)
        else:
          outString += "      "
        i+=1

      outString += "\nLetters Played"
      outString += "\nMe: {}".format(self.play_dict['me']['tiles'])
      outString += "\n{}: {}".format(self.op, self.play_dict['op']['tiles'])

      return outString
      



#foo
