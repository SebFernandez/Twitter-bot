from credential_bot import *
from tweepy import *
import time, re, random
from datetime import datetime

def sentence ():
	art = ['El', 'La', 'Tu', 'Yo', 'Los', 'Las', 'Nosotros']
	verbs = ['jugar', 'robar', 'saltar', 'cocinar', 'cortar', 'pintar']
	adj = ['grande', 'gordo', 'chico', 'alto', 'hueco', 'profundo']
	r1 = random.randrange (0, 7)
	r2 = random.randrange (0, 6)
	r3 = random.randrange (0, 6)
	phrase = art [r1] + ' ' + verbs [r2] + ' ' + adj [r3] + '.'
	return phrase 

def read_ids():
	f = open("IDS.txt", "r")
	ids = f.read()
	f.close()
	return ids

def write_id(id):
	f = open("IDS.txt", "w")
	f.write(str(id))
	f.close()

def log_tweet(x, now):
	msj = "Tweet nro: " + str (x) + "			" + str (now.hour) + ":" + str (now.minute) 
	print (" ")
	print (msj)
	
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

IDS = read_ids()

run = 0
while True:
	now = datetime.now()
	tweets = api.search(q='@Bot_en_gel', since_id = IDS)

	try
		for tweet in tweets:
			tweet.retweet()

			replyname = tweet.user.screen_name
			sent = sentence()
			reply = "@" + replyname + " " + sent

			api.update_status(status = reply)

			print("Tweet contestado: " + reply)
			write_id(tweet.id)

	except TweepError as e:
		print (e.reason)

	except StopIteration:
		break


	if (now.hour % 2 == 0):
		word = 'Chocolate'
	else:
		word = 'Vainilla'
	
	tweet_data = word + ' ' + now.strftime("%H:%M") + '.'
	api.update_status(status = tweet)
	
	log_tweet(run, now)

	time.sleep (1800)
	run = run + 1
