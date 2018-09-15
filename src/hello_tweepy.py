import tweepy
import twitter_credentials
import json
import os
import urllib
import shutil

auth = tweepy.OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_secret)
auth.set_access_token(twitter_credentials.access_token, twitter_credentials.access_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
media_urls = []
for tweet in public_tweets:
    #get json(its in unicode) from status and access as dictionary
    json_dict = tweet._json
    #reading the media object from the entities and extended entities object
    media_list=[]
    if(json_dict.get("entities").get("media")!=None):
        media_list = json_dict.get("entities").get("media")
    elif(json_dict.get("extended_entities")!=None):
        media_list = json_dict.get("extended_entities").get("media")
    #iterating through the media object to look for photos and add media_url to list
    for media in media_list:
        if(media.get("type") == "photo"):
            media_urls.append(media.get("media_url"))

if(len(media_urls)>0):
    print("Images received from Twitter.\n")

#New path for downloading images to
curr_path = os.getcwd()
new_path = curr_path + '/twitter_images'
path_made = False
if not os.path.exists(curr_path+"/twitter_images"):
    print "Creating path for images\n"
    os.makedirs(new_path)
    path_made = True
else:
    print "Path already exists. Please Delete before proceeding\n"

if(path_made):
    os.chdir(new_path)
    urllib.urlretrieve("http://www.gunnerkrigg.com//comics/00000001.jpg", "image0001.jpg")
