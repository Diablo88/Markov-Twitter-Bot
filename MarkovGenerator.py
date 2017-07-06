import random

class Markov(object):
	
	def __init__(self, TextFile):
		self.TextCorpus = TextFile.read()
		self.Words = self.TextCorpus.split()
		self.InitialWords = self.ExtractInitialWords()
		self.Database = {}
		self.CreateDatabse()
		
	def ExtractInitialWords(self):
		Lines = self.TextCorpus.split('\n')
		InitialWords = []
		
		for line in Lines:
			if line == '':
				 continue

			InitialWords.append(line.split()[0])
		
		return InitialWords
		
	def Pairs(self):
		if len(self.Words) < 2:
			return
		
		for i in range(len(self.Words) - 1):
			yield (self.Words[i], self.Words[i+1])
		
		LastWord = self.Words[-1]
		yield (LastWord, '.')
			
	def CreateDatabse(self):
		for Word1, Word2 in self.Pairs():
			self.Database.setdefault(Word1, [])
			self.Database[Word1].append(Word2)
				
	def GenerateMarkovText(self, LengthOfChain=20):
		GeneratedChain = []
		Word1 = random.choice(self.InitialWords)
	
		for i in xrange(LengthOfChain):
			GeneratedChain.append(Word1)
			Word1 = random.choice(self.Database[Word1])
		
		return ' '.join(GeneratedChain)
