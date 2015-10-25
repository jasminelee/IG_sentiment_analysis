import urllib,json
from instagram.client import InstagramAPI

access_token = "251678025.7724d33.79f467adec834d94aca2b87619975301"
client_secret = "d9f0149ef49a4e658016f5acd07372c0"


api = InstagramAPI(access_token=access_token, client_secret=client_secret)
hashtag = api.tag_search('capitalone')[0][0]
tags = api.tag_recent_media(20, None,'capitalone')
data = tags[0] #choose the exact 'capitalone' tag, not the 'capitalonecup' kind of tags. data is a list of Media objects/the last 20 posts

user_ids = map(lambda x: x.user.id, data)

# #how many ppl a user follows
# num_followers, num_posts, num_follows = {}, {}, {}
# for user in user_ids:
# 	url = "https://api.instagram.com/v1/users/" + user + "/?access_token=251678025.7724d33.79f467adec834d94aca2b87619975301"
# 	response = urllib.urlopen(url)
# 	data = json.loads(response.read())
# 	num_followers[user] = data['data']['counts']['followed_by']
# 	num_posts[user] = data['data']['counts']['media']
# 	num_follows[user] = data['data']['counts']['follows']
# 	# 

# print num_followers
# print num_posts
# print num_follows

#sentiment analysis
for media in data:
#	print media.caption.text, #({"text": "I love eating pizza, it's delicious!"})
	stuff = urllib.urlencode({"text": (media.caption.text).encode('utf-8')}) 
	u = urllib.urlopen("http://text-processing.com/api/sentiment/", stuff)
	the_page = u.read()
	print the_page


	# recent_media, next = api.user_recent_media(user_id=user)
	# num_posts = len(recent_media) #initialize number of posts to first page's num posts
	# while next: # add the rest of the pages posts to num posts
	#     more_media, next = api.user_recent_media(with_next_url=next)
	#     recent_media.extend(more_media)
	#     num_posts += len(more_media)
	# num_user_posts[user] = num_posts

# ppl_users_follow = {}
# for user in users:
# 	following, next = api.user_follows(user_id = user) #num ppl user is following
# 	num_following = len(following)
# 	while next:
# 		more_following, next = api.user_follows(with_next_url=next)
# 		following.extend(more_following)
#		num_following += len(more_following)
# 		for user_being_followed in more_following:
# 			num_following+=1
# 	ppl_users_follow[user] = num_following
# #print ppl_users_follow

# number of ppl following a user -- FIX
# users_followers = {}
# for user in users:
# 	followers, next = api.user_followed_by(user_id = user)
# 	num_followers = len(followers)
# 	while next:
# 		more_followers, next = api.user_followed_by(with_next_url=next)
# 		followers.extend(more_followers)
# 		num_followers += len(more_followers)

# 		# for follower in more_followers:
# 		# 	print "ho"
# 		# 	num_followers+=1
# 	users_followers[user] = num_followers
# print users_followers


# person = data[0].user.id # 
# print len(api.user_follows(person)[0]) #number of ppl this user follows. must do [0] bc ds is a tuple
# print len(api.user_followed_by(person)[0]) #number of ppl following this user


#number of posts users have



# for media in data:
# 	print media.likes

# user = api.user_search('crizzlelee')[0].id
# recent_media, next_ = api.user_recent_media(user_id=user, count=10)
# for media in recent_media:
# 	print media.comments
#   print media.caption.text


