class CondFreqDist:
  
  def __init__(self,filename):
    self.conDict = {}
    self.uniDict = {}
    self.totalCons = 0
    self.wordList = []
    corp = open(filename,'r')
    
    for line in corp:
      splinter = line.split( )
      for s in splinter:
        self.wordList.append(s)
        if s in self.uniDict: self.uniDict[s] += 1
        else: self.uniDict[s] = 1
      
    for w in range(len(self.wordList) - 1):
      bigram = (self.wordList[w],self.wordList[w+1])
      a,b = bigram     
      if a not in self.conDict:
        self.conDict[a] = {b : 1}
        self.totalCons += 1
      else:
        if b not in self.conDict[a]:
          self.conDict[a][b] = 1
          self.totalCons += 1
        else:
          self.conDict[a][b] += 1
          self.totalCons += 1
      
    
  def count(self,w1,w2):
    if w1 not in self.conDict: return 0
    elif w2 not in self.conDict[w1]: return 0
    else: return self.conDict[w1][w2]
    
  def freq(self,w1,w2):
    if w1 not in self.conDict: return 0
    elif w2 not in self.conDict[w1]: return 0
    else:
      #probA = float(self.uniDict[w1])/float(self.totalCons)
      probBlA = float(self.conDict[w1][w2])/float(self.uniDict[w1])
      return probBlA


def main():
  confdist = CondFreqDist('austin.token')
  
  print "and she %d %.8f" % (confdist.count("and","she"), confdist.freq("and","she"))
  print "and Mr %d %.8f" % (confdist.count("and",'Mr'), confdist.freq("and",'Mr'))
  print "and herself %d %.8f" % (confdist.count("and",'herself'), confdist.freq("and",'herself'))
  print "and sister %d %.8f" % (confdist.count("and",'sister'), confdist.freq("and",'sister'))
  print "and lady %d %.8f" % (confdist.count("and",'lady'), confdist.freq("and",'lady'))
  print "and manner %d %.8f" % (confdist.count("and",'manner'), confdist.freq("and",'manner'))
  print "and cried %d %.8f" % (confdist.count("and",'cried'), confdist.freq("and",'cried'))
  print "and feelings %d %.8f" % (confdist.count("and",'feelings'), confdist.freq("and",'feelings'))
  print "and pride %d %.8f" % (confdist.count("and",'pride'), confdist.freq("and",'pride'))
  print "and great %d %.8f" % (confdist.count("and",'great'), confdist.freq("and",'great'))
  print "and family %d %.8f" % (confdist.count("and",'family'), confdist.freq("and",'family'))

if __name__ == '__main__':
  main()
