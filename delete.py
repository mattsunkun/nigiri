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

#　”wait_on_rate_limit = True”　利用制限にひっかかた時に必要時間待機する
api=tweepy.API(auth,wait_on_rate_limit=True)

# 検索条件の設定
#min_favesはいいねの件数が最低200件以上のツイートのみを取得する.変更可能
#*****に検索キーワードを入力する

search_word = ' from:mattsunkun1221'
#何件のツイートを取得するか
item_number = 3

#検索条件を元にツイートを抽出
tweets = tweepy.Cursor(api.search_tweets,q=search_word, tweet_mode='extended',result_type="mixed",lang='ja').items(item_number)

tweet_id_list = []
for tweet in tweets:
    tweet_id_list.append({'id': tweet.id, 'text': tweet.full_text})
    
for tweet in tweet_id_list:
    print(tweet['text'])

