import codecs
import datetime
import urllib2
from xml.etree import ElementTree as etree

iss_tracker_link ="http://spotthestation.nasa.gov/sightings/xml_files/India_None_Hyderabad.xml"
read_iss_link = urllib2.urlopen(iss_tracker_link).read()

iss_root = etree.fromstring(read_iss_link)
item = iss_root.findall('channel/item')

iss_desc = []
iss_date_tweet_dict = {}

for entry in item:
	desc = entry.findtext('description')
	iss_desc.append(desc)

for entry in iss_desc:

	entry = entry.replace("<br/>","")
	entry = entry.replace("\n\t\t\t\t","")
	entry = entry.replace("Date: ","")
	
	loc_maxm = entry.find("Maximum")
	loc_time = entry.find("Time")
	loc_duration = entry.find("Duration")
	
	tweet_date = str(datetime.datetime.strptime(entry[:loc_time], "%A %b %d, %Y ").date())
	
	iss_date_tweet_dict[tweet_date] = "The International Space Station is passing overhead on " + entry[:loc_time] + "at "+ entry[loc_time+6:loc_duration] + "for" + entry[loc_duration+9:loc_maxm-1] + ". #Hyderabad"

#IGNORE THIS!
# save_iss_dates = open('iss_overhead_pass.py','w')
# save_iss_dates.write(str(iss_date_tweet_dict))
# save_iss_dates.close()