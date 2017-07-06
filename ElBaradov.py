import MarkovGenerator
import random
import twitter
import codecs
import time


ARABIC_SOURCE = 'db_ar.txt'
ENGLISH_SOURCE = 'db_en.txt'

ENGLISH_RATIO = 0.3 # probability that a tweet is in English

MINUTES_BETWEEN_TWEETS = 10

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''
api = twitter.Api(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


ArabicTextCourpse = codecs.open(ARABIC_SOURCE, encoding = 'utf-8')
ArabicMarkovLink = MarkovGenerator.Markov(ArabicTextCourpse)

EnglishTextCourpse = codecs.open(ENGLISH_SOURCE, encoding = 'utf-8')
EnglishMarkovLink = MarkovGenerator.Markov(EnglishTextCourpse)

while True:
#	try:
		if random.random() <= ENGLISH_RATIO :
			MarkovLink = EnglishMarkovLink
		else:
			MarkovLink = ArabicMarkovLink
	
		GeneratedText = MarkovLink.GenerateMarkovText()[0:139]

		for character in {'.' ,',' ,'!',' '}:
			if character in GeneratedText:
				GeneratedTextList = GeneratedText.split(character)
				GeneratedTextList.pop()
				Tweet = character.join(GeneratedTextList)

		api.PostUpdate(Tweet)
		time.sleep(60 * MINUTES_BETWEEN_TWEETS)

#	except:
#		time.sleep(60)
