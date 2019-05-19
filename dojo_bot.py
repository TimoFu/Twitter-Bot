import tweepy, time

CONSUMER_KEY = 'J1PydBs5SSCh0uiq9k2fkJzLj'
CONSUMER_SECRET = 'Dvs5DNe2ok8KM4jqUxucJ8io6nI4xNN0xvQa48ZgIrrvmdpMNu'
ACCESS_KEY = '1129542510416605184-xZDjc46m4swABIttVTGiZUw1nNJtG2'
ACCESS_SECRET = 'BH5BBmDjWpyGSUZ6HGHY1vU1cL9LSA2Vb9TstvFEAnlSV'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

mentions=api.mentions_timeline()

for mention in mentions:
	print(mention.text, flush=True)
	#api.retweet(mention.id)


for i in range(1,10):
	time.sleep(60)
	api.update_status(str("marry who?") + str(i))

