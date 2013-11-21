import CondFreqDist
import random

def generateBigramSeq(cdist, length, word):
  unilist = [word]
  
  rambo = random.random()
  r = 0.0
  
  temp = word
  for i in range(length-1):
    rambo = random.random()
    r = 0.0
    if temp not in cdist.conDict:
      print ' '.join(unilist)
      break
      #noWord(temp)
    else:
      for potential in cdist.conDict[temp]:
        r += cdist.freq(temp,potential)
        if (r > rambo):
          unilist.append(potential)
          temp = potential
          break
  print ' '.join(unilist)


def main():
  cdist = CondFreqDist.CondFreqDist('austin.token')
  generateBigramSeq(cdist,10,'Jane')
  generateBigramSeq(cdist,10,'Elizabeth')
  generateBigramSeq(cdist,10,'never')
  generateBigramSeq(cdist,10,'always')
  generateBigramSeq(cdist,10,'The')
  
if __name__ == '__main__':
  main()
