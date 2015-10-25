import urllib,json
from instagram.client import InstagramAPI
import pprint

access_token = "251678025.7724d33.79f467adec834d94aca2b87619975301"
client_secret = "d9f0149ef49a4e658016f5acd07372c0"

print "yo"
api = InstagramAPI(access_token=access_token, client_secret=client_secret)

tags = api.tag_recent_media(20, None,'capitalone')
print tags
posts = tags[0] #choose the exact 'capitalone' tag, not the 'capitalonecup' kind of tags. data is a list of Media objects/the last 20 posts
print posts
user_ids = map(lambda x: x.user.id, posts)

# url = "https://api.instagram.com/v1/tags/capitalone/media/recent?access_token=" + access_token
# response = urllib.urlopen(url)
# data = json.loads(response.read())

# for each in data:
# 	print type(each)
# #	each['user']['id'] a
# #pprint.pprint(data['data'])
# users = map(lambda x: x['user']['id'], data['data'])
# print users

# num_followers is the number of followers. num_followers is the number of ppl a user follows. 
# used dictionaries instead of arrays to map user with their information. 
# num_followers, num_posts, num_follows = {}, {}, {}
# for user in user_ids:
# 	url = "https://api.instagram.com/v1/users/" + user + "/?access_token=" + access_token
# 	response = urllib.urlopen(url)
# 	data = json.loads(response.read())
# 	num_followers[user] = data['data']['counts']['followed_by']
# 	num_posts[user] = data['data']['counts']['media']
# 	num_follows[user] = data['data']['counts']['follows']
# 	# 

# print num_followers
# print num_posts
# print num_follows

#used arrays instead of dictionaries in order to maintain the most recent order
analyzed_posts = []
num_likes =[]
for media in posts:
	# sentiment analysis
	sentiment_data = urllib.urlencode({"text": (media.caption.text).encode('utf-8')})
	u = urllib.urlopen("http://text-processing.com/api/sentiment/", sentiment_data)
	the_page = u.read()
	analyzed_posts.append(the_page)
	# get likes
	url = "https://api.instagram.com/v1/media/" + media.id + "/likes?access_token=" + access_token
	response = urllib.urlopen(url)
	like_data = json.loads(response.read())
	num_likes.append(len(like_data['data']))
print num_likes

sentiments = {}
sentiments['neg'] = 0
sentiments['pos'] = 0 
sentiments['neutral'] = 0

for post in analyzed_posts:
	print post[0]['label']
	if post['probability']['label'] == 'neg':
		sentiments['neg'] += 1
	elif post['probability']['label'] == 'pos':
		sentiments['pos'] += 1
	elif post['probability']['label'] == 'neutral':
		sentiments['neutral'] += 1
print sentiments