from credential_bot import *	#Authentication keys for OAUTH.
from tweepy import *
from tweepy import StreamListener, Stream
import time, re, random
from datetime import datetime

#Log to have a look for the tweets tweeted. 
def log_tweet(x, tweet, RN):
	msj = "Tweet: " + tweet
	num = "Nro: " + str (x)
	print (" ")
	print (msj + "              " + num + "       R: " + str (RN))

#OAUTH
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

run = 0

while True:
	now = datetime.now()
	
	#Normal tweets.
	RandWord = random.randrange (0, 11)
	if (now.minute == 0):
		word = 'BOOOOOOOOOOOOOOOOOONG'
	elif (RandWord == 0):
		word = 'Cheese 666'
	elif (RandWord % 2 == 0):
		word = 'Chocolate'
	elif (RandWord % 3 == 0):
		word = 'Vainilla'
	elif (RandWord % 5 == 0):
		word = 'Whiskey'
	elif (RandWord % 7 == 0):
		word = 'Mint'
	elif (RandWord % 1 == 0):
		word = 'Ron'
	
	tweet = word + ' ' + now.strftime("%H:%M") + '.'
	api.update_status(status = tweet)	#Tweet!
	
	log_tweet(run, tweet, RandWord)
	print ("--------------------------------------------------------------------------------")

	run = run + 1
	time.sleep (random.randrange (1,43200))	#Random time. 43200 sec = 12 hours.