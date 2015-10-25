from instagram.client import InstagramAPI

access_token = "251678025.7724d33.79f467adec834d94aca2b87619975301"
client_secret = "d9f0149ef49a4e658016f5acd07372c0"
api = InstagramAPI(access_token=access_token, client_secret=client_secret)
recent_media, next_ = api.user_recent_media(user_id="jasmineleelee", count=10)
for media in recent_media:
   print media.caption.text