import tweepy
import re
import codecs
import datetime


ckey = "5GwwKpM2NvzXCpfn28saSk3CN"
csecret = 'F7UKxhJLNyprK5mNV5bKSiNogvuLJ4X6klfF7LVhwHCRCAUMVk'
atoken = '3145110713-G9HFvOkdf1c7BzmK7IaJTm048DVD3TvgUM20zdb'
asecret = 'VFcZ1whomwbl4IojkIf3krC6u71m7qMyh7Nm69wfjYUFK'
count = 0

auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
api = tweepy.API(auth)

api.update_status()