import tweepy

CONSUMER_KEY = 'MVPC5qfaIzXLBkTPsRCzQ1OkJ'
CONSUMER_SECRET = 'A7LfHw0MkgxiOgvXHdASG1NulJUanaVfXLOS3DMu43Bmt5YjlM'
ACCESS_TOKEN = '1371334274603913216-UzWHOx82xdMueEGJsql0V6swcIFxpK'
ACCESS_SECRET = 'lHfLiYEWIVxws2Qc3sHtdOVqe8NMwdp3WCcnUIYSI9H9N'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)