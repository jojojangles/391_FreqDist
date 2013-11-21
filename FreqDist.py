class FreqDist:
  
  def __init__(self,filename):
    self.wordCount = {}
    self.totalWords = 0
    corp = open(filename,'r')
    
    for line in corp:
      for word in line.split(' '):
        if not(word in self.wordCount):
          self.wordCount[word] = 1
          self.totalWords += 1
        else:
          self.wordCount[word] += 1
          self.totalWords += 1
      
    
  def count(self,word):
    return self.wordCount[word]
    
  def freq(self,word):
    return float(self.wordCount[word])/float(self.totalWords)
    
  def corpusLengthCheck(self):
    print len(self.wordCount)

def main():
  fdist = FreqDist('austin.token')
  
  fdist.corpusLengthCheck()
  print "she %d %.8f" % (fdist.count("she"), fdist.freq("she"))
  print "Mr %d  %.8f" % (fdist.count('Mr'), fdist.freq('Mr'))
  print "herself %d  %.8f" % (fdist.count('herself'), fdist.freq('herself'))
  print "sister %d  %.8f" % (fdist.count('sister'), fdist.freq('sister'))
  print "lady %d  %.8f" % (fdist.count('lady'), fdist.freq('lady'))
  print "manner %d  %.8f" % (fdist.count('manner'), fdist.freq('manner'))
  print "cried %d  %.8f" % (fdist.count('cried'), fdist.freq('cried'))
  print "feelings %d  %.8f" % (fdist.count('feelings'), fdist.freq('feelings'))
  print "pride %d  %.8f" % (fdist.count('pride'), fdist.freq('pride'))
  print "great %d  %.8f" % (fdist.count('great'), fdist.freq('great'))
  print "family %d  %.8f" % (fdist.count('family'), fdist.freq('family'))
  print "home %d  %.8f" % (fdist.count('home'), fdist.freq('home'))
  print "character %d  %.8f" % (fdist.count('character'), fdist.freq('character'))
  print "letter %d  %.8f" % (fdist.count('letter'), fdist.freq('letter'))
  print "happiness %d  %.8f" % (fdist.count('happiness'), fdist.freq('happiness'))
  print "party %d  %.8f" % (fdist.count('party'), fdist.freq('party'))
  print "means %d  %.8f" % (fdist.count('means'), fdist.freq('means'))
  print "acquaintance %d  %.8f" % (fdist.count('acquaintance'), fdist.freq('acquaintance'))
  print "woman %d  %.8f" % (fdist.count('woman'), fdist.freq('woman'))
  
if __name__ == '__main__':
  main()
