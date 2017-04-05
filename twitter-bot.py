from credential_bot import *	#Authentication keys for OAUTH.
from tweepy import *
import time, re, random
from datetime import datetime

#Random sentences are generated.
def sentence ():
	art = ['El', 'La', 'Tu', 'Yo', 'Los', 'Las', 'Nosotros']
	verbs = ['jugar', 'robar', 'saltar', 'cocinar', 'cortar', 'pintar', 'absorber', 'bendecir', 'freir', 'poseer', 'sujetar', 'decir', 'prender', 'imprimir']
	adj = ['grande', 'gordo', 'chico', 'alto', 'hueco', 'profundo', 'amargo', 'muerto', 'mojado', 'dormido', 'feo']
	r1 = random.randrange (0, len (art))
	r2 = random.randrange (0, len (verbs))
	r3 = random.randrange (0, len (adj))
	phrase = art [r1] + ' ' + verbs [r2] + ' ' + adj [r3] + '.'
	return phrase 

#Checks tweet ID to know if it has to RT and reply.
def read_ids():
	f = open("IDS.txt", "r")
	ids = f.read()
	ids = int (ids)
	f.close()
	return ids

#Once it replies and RT, writes the tweet ID
def write_id(id):
	f = open("IDS.txt", "w")
	f.write(str(id))
	f.close()

#Log to have a look for the tweets tweeted. 
def log_tweet(x, tweet):
	msj = "Tweet: " + tweet
	num = "Nro: " + str (x)
	print (" ")
	print (msj + "              " + num)

#Log for the replying tweet.
def info_tweet (replyname, text, reply):
	print ("\t\tUser   : " + replyname)
	print ("\t\tMention: " + tweet.text)
	print ("\t\tAnswer : " + reply + "\n\n")

#When there is a tweet saying 'draw!', replies with a drawing.
def drawing ():
	line = ['_____\O/________/\________', '----{,_,">', '@( * O * )@', '-@-@-', '(-.-)Zzz...', 'c[_]']
	return line [random.randrange (0, len(line))]

#OAUTH
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

IDS = read_ids()


run = 1		#run is the counter of tweets tweeted
while True:
	now = datetime.now()
	tweets = api.search(q='@Bot_en_gel', since_id = IDS) #Looks for mentions.

	for tweet in tweets:
		try:	
			if re.search ('^@Bot_en_gel', tweet.text):
				tweet.retweet()

				if (tweet.text == "@Bot_en_gel hola." or tweet.text == "@Bot_en_gel hola"):
					replyname = tweet.user.screen_name
					R = random.randrange (0, 2)
					if (R == 0):
						sent = "Hola!"
						reply = "@" + replyname + " " + sent
						
						api.update_status(status = reply)	#Tweet!

						info_tweet (replyname, tweet.text, reply)

						write_id(tweet.id)
					else:
						sent = "Chau chau!"
						reply = "@" + replyname + " " + sent
						
						api.update_status(status = reply)	#Tweet!

						info_tweet (replyname, tweet.text, reply)

						write_id(tweet.id)

				elif (tweet.text == "@Bot_en_gel hello." or tweet.text == "@Bot_en_gel hello"):
					replyname = tweet.user.screen_name
					R = random.randrange (0, 2)
					if (R == 0):
						sent = "Hey!"
						reply = "@" + replyname + " " + sent
						
						api.update_status(status = reply)	#Tweet!

						info_tweet (replyname, tweet.text, reply)

						write_id(tweet.id)
					else:
						sent = "XOXO."
						reply = "@" + replyname + " " + sent
						
						api.update_status(status = reply)	#Tweet!

						info_tweet (replyname, tweet.text, reply)

						write_id(tweet.id)
				elif (tweet.text == "@Bot_en_gel puto." or tweet.text == "@Bot_en_gel puto" or tweet.text == "@Bot_en_gel puta." or tweet.text == "@Bot_en_gel puta"):
					replyname = tweet.user.screen_name
					sent = "puto."
					reply = "@" + replyname + " " + sent
					api.update_status(status = reply)	#Tweet!

					info_tweet (replyname, tweet.text, reply)

					write_id(tweet.id)

				elif (tweet.text == "@Bot_en_gel draw!"):
					replyname = tweet.user.screen_name	#Gets the user name.
					sent = drawing ()
					reply = "@" + replyname + " " + sent

					api.update_status(status = reply)	#Tweet!

					info_tweet (replyname, tweet.text, reply)

					write_id(tweet.id)

				elif (tweet.text == "@Bot_en_gel scream!"):
					replyname = tweet.user.screen_name
					sent = random.randrange (1,10) * 'A' + random.randrange (1,10) * 'H'
					reply = "@" + replyname + " " + sent

					api.update_status(status = reply)	#Tweet!

					info_tweet (replyname, tweet.text, reply)

					write_id(tweet.id)

				else:
					replyname = tweet.user.screen_name	#Gets the user name.
					sent = sentence()
					reply = "@" + replyname + " " + sent

					api.update_status(status = reply)	#Tweet!

					info_tweet (replyname, tweet.text, reply)

					write_id(tweet.id)

		#Stops the iteration and put in the log the error.
		except TweepError as e:
			print ("\n\n>>>\tUser: @" + tweet.user.screen_name + "   status: " +str (tweet.id) + "   time: " + str (tweet.created_at))
			print (">>>\t" + tweet.text)
			print (">>>\t" + e.reason)

		except StopIteration:
			break

	#Normal tweets.
	RandWord = random.randrange (0, 11)
	if (now.minute == 0):
		word = 'BOOOOOOOOOOOOOOOOOONG'
	elif (RandWord % 2 == 0):
		word = 'Chocolate'
	elif (RandWord % 3 == 0):
		word = 'Vainilla'
	elif (RandWord % 5 == 0):
		word = 'Whiskey'
	elif (RandWord % 7 == 0):
		word = 'Mint'
	elif (RandWord == 0):
		word = 'Cheese 666'
	
	tweet = word + ' ' + now.strftime("%H:%M") + '.'
	api.update_status(status = tweet)	#Tweet!
	
	log_tweet(run, tweet)
	print ("--------------------------------------------------------------------------------")

	run = run + 1
	time.sleep (random.randrange (1,43200))	#Random time. 43200 sec = 12 hours.