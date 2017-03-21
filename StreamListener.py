from credential_bot import *	#Authentication keys for OAUTH.
from tweepy import *
from tweepy import StreamListener, Stream
from datetime import datetime

#OAUTH
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

class CustomStreamListener(StreamListener):

	def on_status (self, status):
		#print (data)
		record = {'Text': status.text, 'User': status.author.screen_name, 'Time': str (status.created_at)}
		print ("U: " + record ['User'] + "\n" + "T: " +  record ['Text'] + "\n" + 'H: ' + record ['Time'])
		print ("--------------------------------------------------------------------------------\n")

	def on_error(self, status_code):
		print (status_code)
		if status_code == 420:
			return False #returning False in on_data disconnects the stream

if __name__ == '__main__':
    listener = CustomStreamListener()
    twitterStream = Stream(auth, listener)
    twitterStream.filter(follow=['XXXXX'])