import pandas as pd
from mtranslate import translate
import pickle

#path = r'C:\Users\sociocom\Desktop\Crawler\backup\31May-4June 2018'
path = r"/home/wannita/crawler/backup/31May-4June 2018"

def save_obj(file, obj):
    with open(file, 'wb') as f:
        pickle.dump(obj, f)

def load_obj(file):
    with open(file, 'rb') as f:
        return pickle.load(f)

def open_to_pandas(spath):
    tweets = open(path + spath, "r", encoding="utf-8")
    tweets_list = []
    for line in tweets:
        tweets_list.append(line.split('\t'))
    labels = ['acc_id','acc','tweet_id','text','created_time','ex_lat','ex_long','place','lot_sw','lot_ne','tweet_reply_id','tweet_reply_user_id','tweet_reply_username','lang']
    name = pd.DataFrame(tweets_list,columns=labels)
    filt = ((name["lang"] == "th\n") | (name["lang"] == "en\n") | (name["lang"] == "ja\n") | (name["lang"] == "de\n") | (name["lang"] == "pt\n"))
    name = name[filt]
    name['lang'] = name['lang'].apply(lambda x: x.strip())
    print("all data :" ,len(name), "tweets")
    return name

df_sfc = open_to_pandas("/SFC_en_tweets.txt")
save_obj(path + '/translated_sfc_tweet', df_sfc)
