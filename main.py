import urllib,json
from instagram.client import InstagramAPI
import pprint

access_token = "251678025.7724d33.79f467adec834d94aca2b87619975301"
client_secret = "d9f0149ef49a4e658016f5acd07372c0"
hashtag = "capitalone"

api = InstagramAPI(access_token=access_token, client_secret=client_secret)
tags = api.tag_recent_media(20, None, hashtag)
posts = tags[0] #choose the exact 'capitalone' tag, not the 'capitalonecup' kind of tags. data is a list of Media objects/the last 20 posts
user_ids = map(lambda x: x.user.id, posts)

# num_followers is the number of followers. num_followers is the number of ppl a user follows. 
# used dictionaries instead of arrays to map user with their information. 
num_followers, num_posts, num_follows = {}, {}, {}
for user in user_ids:
	url = "https://api.instagram.com/v1/users/" + user + "/?access_token=" + access_token
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	num_followers[user] = data['data']['counts']['followed_by']
	num_posts[user] = data['data']['counts']['media']
	num_follows[user] = data['data']['counts']['follows']

print "The number of followers these users have: {}".format(num_followers)
print "The number of posts these users have: {}".format(num_posts)
print "The number of people these users follows: {}".format(num_follows)

#used arrays instead of dictionaries in order to maintain the most recent order
analyzed_posts = []
num_likes =[]
sentiments = []

for media in posts:
	sentiment analysis
	sentiment_data = urllib.urlencode({"text": (media.caption.text).encode('utf-8')})
	u = urllib.urlopen("http://text-processing.com/api/sentiment/", sentiment_data)
	the_page = json.loads(u.read())
	sentiments.append(the_page['label'])
	get likes
	url = "https://api.instagram.com/v1/media/" + media.id + "/likes?access_token=" + access_token
	response = urllib.urlopen(url)
	like_data = json.loads(response.read())
	num_likes.append(len(like_data['data']))

neg_sentiments, pos_sentiments, neutral_sentiments  = 0, 0, 0

for label in sentiments:
	if label == 'neg':
		neg_sentiments +=1
	elif label == 'pos':
		pos_sentiments += 1
	elif label == 'neutral':
		neutral_sentiments += 1

print "The like count for each post: {}".format(num_likes)
print "Number of posts that are negative: {}, postive: {}, neutral: {}".format(neg_sentiments, pos_sentiments, neutral_sentiments)