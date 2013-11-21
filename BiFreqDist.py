class BiFreqDist:
  
  def __init__(self,filename):
    self.biCount = {}
    self.totalBis = 0
    self.wordList = []
    corp = open(filename,'r')
    
    for line in corp:
      splinter = line.split( )
      for s in splinter:
        self.wordList.append(s)
      
    for w in range(len(self.wordList) - 1):
      bigram = (self.wordList[w],self.wordList[w+1])
           
      if bigram not in self.biCount:
        self.biCount[bigram] = 1
        self.totalBis += 1
      else:
        self.biCount[bigram] += 1
        self.totalBis += 1
      
    
  def count(self,w1,w2):
    if (w1,w2) not in self.biCount: return 0
    else: return self.biCount[(w1,w2)]
    
  def freq(self,w1,w2):
    if (w1,w2) not in self.biCount: return 0
    else: return float(self.biCount[(w1,w2)])/float(self.totalBis)
    
  def testprint(self):
    print self.biCount

def main():
  bifdist = BiFreqDist('austin.token')
  
  print "and she %d %.8f" % (bifdist.count("and","she"), bifdist.freq("and","she"))
  print "and Mr %d %.8f" % (bifdist.count("and",'Mr'), bifdist.freq("and",'Mr'))
  print "and herself %d %.8f" % (bifdist.count("and",'herself'), bifdist.freq("and",'herself'))
  print "and sister %d %.8f" % (bifdist.count("and",'sister'), bifdist.freq("and",'sister'))
  print "and lady %d %.8f" % (bifdist.count("and",'lady'), bifdist.freq("and",'lady'))
  print "and manner %d %.8f" % (bifdist.count("and",'manner'), bifdist.freq("and",'manner'))
  print "and cried %d %.8f" % (bifdist.count("and",'cried'), bifdist.freq("and",'cried'))
  print "and feelings %d %.8f" % (bifdist.count("and",'feelings'), bifdist.freq("and",'feelings'))
  print "and pride %d %.8f" % (bifdist.count("and",'pride'), bifdist.freq("and",'pride'))
  print "and great %d %.8f" % (bifdist.count("and",'great'), bifdist.freq("and",'great'))
  print "and family %d %.8f" % (bifdist.count("and",'family'), bifdist.freq("and",'family'))
  

if __name__ == '__main__':
  main()
