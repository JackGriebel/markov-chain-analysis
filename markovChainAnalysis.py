import random

class Word():
	def __init__(self, word):
		self.word = word
		self.followingWords = []
		
	def addWord(self, word):
		self.followingWords.append(word)
	
	def getWords(self):
		return self.followingWords
	
	def str(self):
		return self.word + ", " + str(self.mostCommonFollowing())
	
	def getWord(self):
		return self.word
	
	def mostCommonFollowing(self):
		wordOccurances = {}
		for str in self.followingWords:
			if str in wordOccurances:
				wordOccurances[str] += 1
			else:
				wordOccurances[str] = 1
		mostCommonWord = "NEXT WORD NOT FOUND"
		mostCommonWordOccurances = -1		
		for key,value in wordOccurances.items():
			if value > mostCommonWordOccurances:
				mostCommonWord = key
				mostCommonWordOccurance = 0
		return mostCommonWord
	
	def scrubWord(self, word):
		while word in self.followingWords:
			self.followingWords.remove(word)
		try:
			self.followingWords.remove(word)
		except:
			i = 0

class text():
	def __init__(self, filePath):
		self.path = filePath
		self.wordList = self.parseText(self.path)
		self.wordDictionary = self.generateWordDictionary(self.path)

	def parseText(self, fileLocation):
		with open(fileLocation) as file_object:
			book = file_object.read()
			lines = book.split('\n')
			words = []
			for line in lines:
				lineSplit = line.split(' ')
				for word in lineSplit:
					word = word.replace('.', '')
					word = word.replace(',', '')
					word = word.replace(';', '')
					word = word.replace('?', '')
					word = word.replace('!', '')
					word = word.replace(':', '')
					word = word.replace('"', '')
					word = word.replace(' ', '')
					words.append(word.lower())
			return words	

	def generateWordDictionary(self, fileLocation):
		wordDict = {}
		words = self.wordList
		for num in range(0, len(words) - 1):
			currentWord = words[num].lower()
			if currentWord in wordDict:
				wordDict[currentWord].addWord(words[num + 1].lower())
			else:
				wordDict[currentWord] = Word(currentWord)
				wordDict[currentWord].addWord(words[num + 1].lower())
		return wordDict

	def getStartingWord(self):
		return random.choice(self.wordList)
	
	def printWords(self, numTimes, word='NONE', wordDict={}, saidWords=[]):
		if word == 'NONE':
			word = self.getStartingWord()
		if not wordDict:
			wordDict = self.wordDictionary.copy()
		nextWord = wordDict[word].mostCommonFollowing()
		wordDict[word].scrubWord(nextWord)
		if word != '':
			print(word, end=" ")
		saidWords.append(word)
		if numTimes != 0:
			self.printWords(numTimes - 1, nextWord, wordDict, saidWords)


print("Romeo And Juliet:\n")

romeo = text('romeo and juliet.txt')
romeo.printWords(20)

print('\n\n\nCall Of The Wild:\n')

call = text('call of the wild.txt')
call.printWords(20)

print('\n\n\nOn The Origin Of Species:\n')

origin = text('origin of species.txt')
origin.printWords(20)

print('\n\n\nThe Fedralist Papers:\n')

federalist = text('federalist papers.txt')
federalist.printWords(20)

print('\n\n\nThe Communist Manifesto:\n')

maifesto = text('communist manifesto.txt')
maifesto.printWords(20)
