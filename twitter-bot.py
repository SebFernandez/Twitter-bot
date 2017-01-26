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

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

f = open ("IDS.txt", "r")
IDS = f.read ()
#IDS = int (IDS)
f.close()

x = 0
while True:
	now = datetime.now()
	twts = api.search (q='@Bot_en_gel', since_id = IDS)

	for t in twts:
		if re.search ('^@Bot_en_gel', t.text):
			try:
				t.retweet ()
			except TweepError as e:
				print (e.reason)

			except StopIteration:
				break

			replyname = t.user.screen_name
			sent = sentence ()
			reply = "@" + replyname + " " + sent
			api.update_status (status = reply)
			print ("Tweet contestado")
			print "                 " + reply
			IDS = t.id
			f = open ("IDS.txt", "w")
			f.write (str (IDS))
			f.close ()

	if (now.hour % 2 == 0):
		x = x + 1
		tweet = 'Chocolate ' + str (now.hour) + ':' + str (now.minute) + '.'
	else:
		x = x + 1
		tweet = 'Vainilla ' + str (now.hour) + ':' + str (now.minute)	+ '.'

	api.update_status(status = tweet)
	msj = "Tweet nro: " + str (x) + "			" + str (now.hour) + ":" + str (now.minute) 
	print (" ")
	print (msj)

	time.sleep (1800)

'''
for tweet in Cursor (api.search, q='Star Wars').items():
	try:
		print ('\nTweet by: @' + tweet.user.screen_name)

		tweet.retweet()
		print ('\t\t\tRetweeted the tweet')

		time.sleep (1800)

	except TweepError as e:
		print (e.reason)

	except StopIteration:
		break


		tweet.favorite ()
		print ('\t\t\tFavorited the tweet')
'''