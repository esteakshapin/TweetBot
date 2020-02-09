rl = []
txt = []
import re
parse = [(re.sub(r'[a-z]*[:.]+\S+', '', i.split(",")[1]), i.split(",")[3], i.split(",")[4], i.split(",")[2]) for i in open("tweets.csv", "r", encoding="utf8").read().split("\n")]
rts = []
favs = []
times = []
tweets = []
for i in parse:
    txt.append(i[0])
    rts.append(i[1])
    favs.append(i[2])
    times.append(i[3])
    rl.append(i)
import markovify
j = "\n".join(txt)
markov = markovify.Newlinetxt(j)
from random import random, choice
def m():
    tweet = {"txt": None, "rtw": None, "fv": None, "ir?": None, "date": None}
    from datetime import datetime
    if(random() > 0.7):
        rl = choice(rl)
        tweet["rtw"] = choice(rts)
        tweet["fv"] = choice(rts)
        tweet["ir?"] = False
        tweet["txt"] = rl[0].replace("&amp", "&")
        date = rl[3]
        tweet["date"] = datetime.strftime(datetime.strptime(date, '%m-%d-%Y %H:%M:%S'),'%#I:%M %p - %d %b %Y')
    else:
        generated = markov.make_short_sentence(int(50 + random()*150))
        tweet["rtw"] = choice(rts)
        tweet["fv"] = choice(rts)
        tweet["ir?"] = False
        tweet["txt"] = generated.replace("&amp;", "&")
        date = choice(times)
        tweet["date"] = datetime.strftime(datetime.strptime(date, '%m-%d-%Y %H:%M:%S'), '%#I:%M %p - %d %b %Y')
    return tweet
