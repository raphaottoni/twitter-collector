import tweepy
#import twitter dev account informaiton
from config import *
import gzip
import json
from multiprocessing import Pool

# oAuth authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#para ja voltar parseado
#api = tweepy.API(auth)

#Para voltar como json
api = tweepy.API(auth,parser=tweepy.parsers.JSONParser())

def getTweets(user):
    print "Coletando userrrrrrrrrrrrr " +  user
    timeline = api.user_timeline(screen_name=user, count=200)
    tweetsSaida = gzip.open("./profiles/"+user+".gz","a")
    already_collectedFile = open(output_filename,"a")
    while timeline:
        for tweet in timeline:
            #print tweet.keys()
            #print "lastId " +  str(tweet["id"])
            tweet["text"] = tweet["text"].encode("UTF-8")
            #print tweet["text"]
            json.dump(tweet,tweetsSaida)
            tweetsSaida.write("\n")
            lastID= tweet["id"]
        timeline = api.user_timeline(screen_name=user, count=200, max_id=lastID -1)
    tweetsSaida.close()
    already_collectedFile.write(user+"\n")
    already_collectedFile.close()

# ---- MAIN --- #
output_filename = "./twitterIDs_verificado"
usuariosTotais = open("./twitterIDs","r")

already_collected = set()
all_users= set()

old_file = open(output_filename, "r")
for user_id in old_file:
   already_collected.add(user_id.strip())
old_file.close()

for user in usuariosTotais:
   all_users.add(str(user).strip())

#select the remaining days to parse
to_collect = all_users.difference(already_collected)

print "Remaning: " + str(len(to_collect))

p= Pool(processes=1)
p.map(getTweets,list(to_collect))

