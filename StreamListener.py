from credential_bot import *	#Authentication keys for OAUTH.
from tweepy import *
from tweepy import StreamListener, Stream
from datetime import datetime

#OAUTH
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

'''
	Clarin 		--> 8105922
	La nacion 	--> 33989170
	Infobae		-->	69416519
	Metro 95.1  --> 69403126
	Blue 100.7  --> 250671743
	Zeby95		--> 179366418
	Bot 		--> 823994056829177856
'''

'''

    text: the text of the tweet itself
    created_at: the date of creation
    favorite_count, retweet_count: the number of favourites and retweets
    favorited, retweeted: boolean stating whether the authenticated user (you) have favourited or retweeted this tweet
    lang: acronym for the language (e.g. “en” for english)
    id: the tweet identifier
    place, coordinates, geo: geo-location information if available
    user: the author’s full profile
    entities: list of entities like URLs, @-mentions, hashtags and symbols
    in_reply_to_user_id: user identifier if the tweet is a reply to a specific user
    in_reply_to_status_id: status identifier id the tweet is a reply to a specific status
'''

class CustomStreamListener(StreamListener):

	def on_status (self, status):
		record = {'Text': status.text, 'User': status.author.screen_name, 'Time': str (status.created_at)}
		print ("U: " + record ['User'] + "\n" + "T: " +  record ['Text'] + "\n" + 'H: ' + record ['Time'])
		print ("--------------------------------------------------------------------------------\n")

	def on_error(self, status_code):
		print (status_code)
		if status_code == 420:
			return False #returning False in on_data disconnects the stream.

if __name__ == '__main__':
    listener = CustomStreamListener()
    twitterStream = Stream(auth, listener)
    twitterStream.filter(follow=['8105922', '33989170', '69416519'])	#Here goes the Twitter ID.