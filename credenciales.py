import tweepy

#Almacenamos las claves otorgadas por Twitter.
CONSUMER_KEY = "pog0xpFJlfR8GxDx4B9jIuEQA"
CONSUMER_SECRET = "llr0UMQ03lkKB8uO2fPKNAg98mdty0xlbtIqLVthW0P01tz2Bl"
ACCESS_KEY = "1320383793191096320-HGg4JownqCLASyHbLou5GXdGwDfgWR"
ACCESS_SECRET = "Z2YXtL14OotBR2GVoxxxxY9VybfqwSBUQJhOGMbTS2VJp"

#Autenticacion en Twitter.
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)