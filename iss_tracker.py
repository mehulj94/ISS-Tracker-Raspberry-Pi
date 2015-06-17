import tweepy
import datetime
import iss_tracker_file_gen

ckey = ''		#Consumer Key from Twitter
csecret = ''	#Consumer secret from Twitter
atoken = ''		#Access Key from Twitter
asecret = ''	#Access secret from Twitter

ISS_data = iss_tracker_file_gen.iss_date_tweet_dict

First_Key = ISS_data.iterkeys().next()
Next_Iss_visit = datetime.datetime.strptime(First_Key , '%Y-%m-%d').date()
Today = datetime.date.today()

time_to_iss_visit = abs(Next_Iss_visit - Today)
days = time_to_iss_visit.days

if days < 2:
	auth = tweepy.OAuthHandler(ckey,csecret)
	auth.set_access_token(atoken,asecret)
	api = tweepy.API(auth)
	
	api.update_status(status = ISS_data.itervalues().next().encode('ascii','ignore'))
	#print ISS_data.itervalues().next().encode('ascii','ignore')
	
# else:
	# print 'Days left for Iss visit is: '+ str(days)
	# print ISS_data
#Uncomment above if you want to see output on command line
