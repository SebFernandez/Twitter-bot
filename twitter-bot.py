from credential_bot import *
from tweepy import *
import time, re, random
from datetime import datetime

def sentence ():
	art = ['El', 'La', 'Tu', 'Yo', 'Los', 'Las', 'Nosotros']
	verbs = ['jugar', 'robar', 'saltar', 'cocinar', 'cortar', 'pintar', 'absorber', 'bendecir', 'freir', 'poseer', 'sujetar', 'decir', 'prender', 'imprimir']
	adj = ['grande', 'gordo', 'chico', 'alto', 'hueco', 'profundo', 'amargo', 'muerto', 'mojado', 'dormido', 'feo']
	r1 = random.randrange (0, len (art))
	r2 = random.randrange (0, len (verbs))
	r3 = random.randrange (0, len (adj))
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
	msj = "Tweet nro: " + str (x) + "			" + now.strftime("%H:%M") 
	print (" ")
	print (msj)

def info_tweet (replyname, text, reply):
	print ("\t\tUser   : " + replyname)
	print ("\t\tMention: " + tweet.text)
	print ("\t\tAnswer : " + reply + "\n\n")

def drawing ():
	line = ['_____\O/________/\________', '----{,_,">', '@( * O * )@', '-@-@-', '(-.-)Zzz...', 'c[_]']
	return line [random.randrange (0, len(line))]

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

IDS = read_ids()

run = 0
while True:
	now = datetime.now()
	tweets = api.search(q='@Bot_en_gel', since_id = IDS)

	for tweet in tweets:
		try:	
			if re.search ('^@Bot_en_gel', tweet.text):
				tweet.retweet()

				if (tweet.text == "@Bot_en_gel draw!"):
					replyname = tweet.user.screen_name
					sent = drawing ()
					reply = "@" + replyname + " " + sent

					api.update_status(status = reply)

					info_tweet (replyname, tweet.text, reply)

					write_id(tweet.id)

				else:
					replyname = tweet.user.screen_name
					sent = sentence()
					reply = "@" + replyname + " " + sent

					api.update_status(status = reply)

					info_tweet (replyname, tweet.text, reply)

					write_id(tweet.id)

		except TweepError as e:
			print ("\n\n>>>\tUser: @" + tweet.user.screen_name + "   status: " +str (tweet.id) + "   time: " + str (tweet.created_at))
			print (">>>\t" + tweet.text)
			print (">>>\t" + e.reason)

		except StopIteration:
			break


	if (now.hour % 2 == 0):
		word = 'Chocolate'
	else:
		word = 'Vainilla'
	
	tweet = word + ' ' + now.strftime("%H:%M") + '.'
	api.update_status(status = tweet)
	
	log_tweet(run, now)
	print ("--------------------------------------------------------------------------------")

	run = run + 1
	time.sleep (1800)