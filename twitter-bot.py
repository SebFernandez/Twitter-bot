from credential_bot import *	#Authentication keys for OAUTH.
from tweepy import *
import requests, time, random

#Log to have a look for the tweets tweeted. 
def log_tweet(x, word):
	msj = "Tweet: " + word
	num = "Nro: " + str (x)
	print (msj)
	print (num)

#OAUTH
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

run = 0

while True:	
	Norris = requests.get('http://api.icndb.com/jokes/random').json()['value']['joke']
	if (len (Norris) <= 140):
		word = Norris
		break

api.update_status(status = word)	#Tweet!
log_tweet(run, word)
print ("--------------------------------------------------------------------------------")

run = run + 1
time.sleep (random.randrange (1,14400))	#Random time. 14400 sec = 4 hours.