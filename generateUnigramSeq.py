import FreqDist
import random

def generateUnigramSeq(fdist, length):
  counter = 0
  unilist = []
  
  rambo = random.random()
  r = 0.0
  for key in fdist.wordCount:
    if(r < rambo):
      r += fdist.freq(key)
    else:
      unilist.append(key)
      counter += 1
    if(counter == length):
      print ' '.join(unilist)
def main():
  fdist = FreqDist.FreqDist('austin.token')
  generateUnigramSeq(fdist,20)
  
if __name__ == '__main__':
  main()
