import tweepy
import random
import datetime

CONSUMER_KEY = 'MVPC5qfaIzXLBkTPsRCzQ1OkJ'
CONSUMER_SECRET = 'A7LfHw0MkgxiOgvXHdASG1NulJUanaVfXLOS3DMu43Bmt5YjlM'
ACCESS_TOKEN = '1371334274603913216-UzWHOx82xdMueEGJsql0V6swcIFxpK'
ACCESS_SECRET = 'lHfLiYEWIVxws2Qc3sHtdOVqe8NMwdp3WCcnUIYSI9H9N'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# api.update_status("hello world!")

nigiri_name_list = ["妖怪にぎり見習い", "妖怪にぎり変化", "妖怪にぎり親方", "妖怪にぎり元締"]
nigiri_skill_list = ["見習いなのでまだ握れない", "``をおにぎりに"]

t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)

# api.update_profile(name=f"今APIを使っています.")
api.update_status(f"{now.time().strftime('%X')}だゾ\n早く寝ろ")

