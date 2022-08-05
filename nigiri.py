import tweepy
import datetime
import random
import time

import MattsunkunAuthorization

# apiの利用をランダムな時間にしたい．
time.sleep( random.randint(3, 5) )

# 使うアカウントを指定
authorization = MattsunkunAuthorization

# nigiriのレベルリスト
nigiri_name_list = ["妖怪にぎり見習い", "妖怪にぎり変化", "妖怪にぎり親方", "妖怪にぎり元締"]

# 前回のnigiriのレベル，握り対象を読み込む
with open("/Users/mattsunkun/experiment/python/twitter/nigiri_status.txt", "r") as fp:
    _level = fp.readline().strip()
    _item = fp.readline().strip().rstrip(',')
    _name = fp.readline().strip().rstrip(',')    
    # level
    level = int(_level)
    # item
    target_item = _item.split(',')
    # name
    target_name = _name.split(',')

"""握りを募集したい"""
'''
search_word = ' from:mattsunkun1221'
tweets = tweepy.Cursor(authorization.api.search_tweets,q=search_word, tweet_mode='extended',result_type="mixed",lang='ja').items(10)

tweet_id_list = []
for tweet in tweets:
    tweet_id_list.append({'id': tweet.id, 'text': tweet.full_text})
    
for tweet in tweet_id_list:
    print(tweet['text'])
'''

# die, skill, up
nigiri_before = nigiri_name_list[level]
act_rand = random.randrange(10)
# die
if( act_rand < 3 ):
    level = 0
    nigiri_next = nigiri_name_list[level]
    msg = f"{nigiri_before}はおにぎりを喉に詰まらせた!"
# skill
elif( act_rand < 6):
    level += 0
    nigiri_next = nigiri_name_list[level]
    oyakata_skill = 0
    while(1):
        if( level == 0 ):
            msg = f"{nigiri_before}は見習いなのでまだ握れない!"
            break
        elif( level == 1 or oyakata_skill == 1 ):
            item = target_item[ random.randrange( len(target_item) ) ]
            msg = f"{nigiri_before}はおにぎりの息を吐いた!\n{item}はおにぎりになってしまった!"
            break
        elif( level == 2 or oyakata_skill == 2 ):
            name = target_name[ random.randrange( len(target_name) ) ]
            msg = f"{nigiri_before}はおにぎりの息を吐いた!\n{name}はおにぎりになってしまった!"
            break
        else:
            oyakata_skill = random.randrange(1, 3)
            continue
# up
else:
    if( level < 3 ):
        level += 1
        nigiri_next = nigiri_name_list[level]
        msg = f"{nigiri_before}はおにぎりのワナを踏んだ!\n{nigiri_before}はレベルが上がって{nigiri_next}になった!"
    else:
        level += 0
        nigiri_next = nigiri_name_list[level]
        msg = f"{nigiri_before}はおにぎりのワナを踏んだ!\n{nigiri_before}は元気になった!"

# nigiri_status.txtの更新
with open("/Users/mattsunkun/experiment/python/twitter/nigiri_status.txt", "w") as fp:
    # level
    print(f"{level}", file=fp)
    # item
    for item in target_item:
        print(f"{item}", end=",", file=fp)
    
    print("", file=fp)
    
    # name
    for name in target_name:
        print(f"{name}", end=",", file=fp)


"""画像もできたら貼りたい"""

# 登録名
# メンションと共に，"「○◯」を握って!"と投稿してください!
# 2:22に一度何かを握ります
# 投稿と共にnigiriの映像も流したい．
# botアカウントを作りたい(1時間に一回何かを握りたい)
authorization.api.update_profile(name=f"{nigiri_next}", description=f' 妖怪握り変化のbot作成中です. 現段階では,朝四時に`握り`に何かが起きます． / #風来のシレン')
# 投稿msg
authorization.api.update_status( msg )


