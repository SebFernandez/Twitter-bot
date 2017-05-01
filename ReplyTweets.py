from credential_bot import *	#Authentication keys for OAUTH.
from tweepy import *
from tweepy import StreamListener, Stream
import time, random
from datetime import datetime

#Log for the replying tweet.
def info_tweet (replyname, text, reply):
	print ("\t\tUser   : " + replyname)
	print ("\t\tMention: " + text)
	print ("\t\tAnswer : " + reply + "\n\n")
	print ("--------------------------------------------------------------------------------")

#When there is a tweet saying 'draw!', replies with a drawing.
def drawing ():
	line = ['_____\O/________/\________', '----{,_,">', '@( * O * )@', '-@-@-', '(-.-)Zzz...', 'c[_]', ')xxxxx[;;;;;;;;;>', 'd[ o_0 ]b', '^(*(oo)*)^', '=^..^=', '<(''<)  <( ' ' )>  (> '')>', '(_8(|)', '((0j0))']
	return line [random.randrange (0, len(line))]

#Random sentences are generated.
def sentence ():
	art = ['El', 'La', 'Tu', 'Yo', 'Los', 'Las', 'Nosotros', 'Aliens']
	verbs = ['jugar', 'robar', 'saltar', 'cocinar', 'cortar', 'pintar', 'absorber', 'bendecir', 'freir', 'poseer', 'sujetar', 'decir', 'prender', 'imprimir', 'aprender', 'perder', 'ganar', 'saltar', 'agitar', 'boludear', 'romper las bolas']
	adj = ['grande', 'gordo', 'chico', 'alto', 'hueco', 'profundo', 'amargo', 'muerto', 'mojado', 'dormido', 'feo', 'malo', 'bueno', 'horrible', 'lindo']
	r1 = random.randrange (0, len (art))
	r2 = random.randrange (0, len (verbs))
	r3 = random.randrange (0, len (adj))
	phrase = art [r1] + ' ' + verbs [r2] + ' ' + adj [r3] + '.'
	return phrase
#Tweets a screaming as a reply
def scream ():
	text = 'A' * random.randrange (0,50) + 'H' *random.randrange (0,50)
	return text

#Tweets a salute as a reply
def greetings ():
	if (random.randrange (0, 5) == 0):
		text = 'Hola!'
	elif (random.randrange (0, 4) == 1):
		text = 'Chau.'
	elif (random.randrange (0, 4) == 2):
		text = 'Hi'
	elif (random.randrange (0, 4) == 3):
		text = 'XOXO.'
	else: 
		text = 'HUEHUEHUEHUEHUEHUE.'
	return text

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

#OAUTH
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

class CustomStreamListener(StreamListener):

	def on_status (self, status):
		mention = {'Text': status.text, 'User': status.author.screen_name, 'ID': status.id}
		TweetText = mention ['Text']
		TweetText = TweetText [0] + TweetText [1:len (TweetText)].lower ()
		if (TweetText [0:11] == '@bot_en_gel' and read_ids() != mention ['ID']):
			#status.retweet()
			write_id (mention['ID'])
			if (TweetText [12:17] == 'draw!' or TweetText [12:16] == 'draw'):
				reply = "@" + mention ['User'] + " " + drawing ()
			elif (TweetText [12:19] == 'scream!' or TweetText [12:18] == 'scream'): 
				reply = "@" + mention ['User'] + " " + scream ()
			elif (random.randrange (0,2) == 0):
				reply = "@" + mention ['User'] + " " + greetings ()
			else:
				reply = "@" + mention ['User'] + " " + sentence ()
		else:
			reply = ''
		if (reply != ''):
			api.update_status(status = reply)	#Tweet!	
		
		info_tweet (str (mention ['User']), str (mention ['Text']), reply)
		write_id (mention ['ID'])


	def on_error(self, status_code):
		print (status_code)
		if status_code == 420:
			return False #returning False in on_data disconnects the stream.

if __name__ == '__main__':
    listener = CustomStreamListener()
    twitterStream = Stream(auth, listener)
    twitterStream.filter(track=['@Bot_en_gel'])	#Here goes the Twitter ID. 