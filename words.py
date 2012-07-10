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

#initial_tiles = {'a': {'count' : 9, 'score' : 1 },
#                'b': {'count' : 2, 'score' : 4 },
#                'c': {'count' : 2, 'score' : 4 },
#                'd': {'count' : 5, 'score' : 2 },
#                'e': {'count' : 13, 'score' : 1 },
#                'f': {'count' : 2, 'score' : 4 },
#                'g': {'count' : 3, 'score' : 3 },
#                'h': {'count' : 4, 'score' : 3 },
#                'i': {'count' : 8, 'score' : 1 },
#                'j': {'count' : 1, 'score' : 10 },
#                'k': {'count' : 1, 'score' : 5 },
#                'l': {'count' : 4, 'score' : 2 },
#                'm': {'count' : 2, 'score' : 4 },
#                'n': {'count' : 5, 'score' : 2 },
#                'o': {'count' : 8, 'score' : 1 },
#                'p': {'count' : 2, 'score' : 4 },
#                'q': {'count' : 1, 'score' : 10 },
#                'r': {'count' : 6, 'score' : 1 },
#                's': {'count' : 5, 'score' : 1 },
#                't': {'count' : 7, 'score' : 1 },
#                'u': {'count' : 4, 'score' : 2 },
#                'v': {'count' : 2, 'score' : 5 },
#                'w': {'count' : 2, 'score' : 4 },
#                'x': {'count' : 1, 'score' : 8 },
#                'y': {'count' : 2, 'score' : 3 },
#                'z': {'count' : 1, 'score' : 10 },
#                '-': {'count' : 2, 'score' : 10 }
#               }
               
class wordsGame:
    
    def __init__(self, player):
      self.startTime = int(time.time())
      self.tiles = initial_tiles 
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



#game = Game('randy')
#game.move('me','ae', 2)
#game.move('op', 'quiz', 22)
#game.end()
