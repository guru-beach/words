# tilepile.py
# Creates a text based tile pile for Words with Friends
#
# Typical usage:
#
# from tilepile import TilePile as tp
# randy =tp('Randy')
# randy.move('me', 'ah' 5)
# randy.move('op', 'ha', 15)
# print randy


import time
import string
import pickle

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

class TilePile(object):
    
    def __init__(self, player):
      """Starts a Words with Friends 'tile pile' interface
       INPUT: Player Name(str)
      """
      self.startTime = int(time.time())
      self.tiles = init_tiles()
      self.op = player
      self.play_dict = {'me': { 'tiles' : [], 'score' : 0.0},
                        'op': { 'tiles' : [], 'score' : 0.0}}

    def move(self, side, letters, score=0.0):
      """Does an actual player move.   Score is optional
      INPUT: side in ['me', 'op'] (op is short for oppenent)
      INPUT: letters in ['lowercase', '--'] (- is blank)
      INPUT: score
      """
      for letter in letters:
        self.tiles[letter][0] -= 1
        self.play_dict[side]['tiles'].append(letter)
      self.play_dict[side]['score'] += score

    def remains(self):
      """Show the remaining tiles for the game"""
      for lower in string.ascii_lowercase+'-':
        count = self.tiles[lower][0]
        if count:
          print "{}:{}".format(lower, count)

    def adjust(self, player, score):
      """Adjusts player score
         INPUT: player in ['me', 'op']
         INPUT: score
      """
      self.play_dict[player]['score'] = score

    def save(self):
      """Saves the object out to a pickle
         WARNING: Doesn't work on IOS (Yet)
      """
      with open('{}.{}'.format(self.op, self.startTime), 'w') as outFile:
        pickle.dump(self, outFile)

    def average(self):
      """Computes score multiplier of Total Score / Total Tile Scores
         This should represent strength of plays
      """
      avgs = []
      for player in ['me', 'op']:
        avg = 0.0
        sum = 0.0
        score = self.play_dict[player]['score']
        tiles = self.play_dict[player]['tiles']
        for tile in tiles:
          sum += self.tiles[tile][1]
        if sum:
          avg = float(score)/float(sum)
        avgs.append(avg)
      return avgs


    def __str__(self):
      """Prints out remaning tiles and the tiles that have been played"""
      outString = ""
      i = 0
      col = 7
      precision = 3
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

      avgs = self.average()
      mescore = self.play_dict['me']['score']
      opscore = self.play_dict['op']['score']
      meavg = avgs[0]
      opavg = avgs[1]
      oplen = len(self.op)
      metiles = self.play_dict['me']['tiles']
      optiles = self.play_dict['op']['tiles']
      outString += "\nPlayer: Score, Score Strength & Letters Played"
      outString += "\n{1:{0}}: {2:3}, {3:2.{5}}, {4}".format(oplen, 'Me', mescore, meavg, metiles, precision)
      outString += "\n{1:{0}}: {2:3}, {3:2.{5}}, {4}".format(oplen, self.op, opscore, opavg, optiles, precision)


      return outString
