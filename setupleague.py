from utils import *
import itertools
import glob
import random
import json
import pprint
import time
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

print("Enter the names of the Players : ")
names = [x for x in input().split()]
print("Generating matchups and perparing avatars")
matchups = [(x,y) for x in names for y in names if x!=y]
h2h = list(itertools.combinations(names,r=2))
getavatars()
avatars = glob.glob('avatars/*')
random.shuffle(matchups)
random.shuffle(avatars)
avatar_rec={}
for i in range(len(names)):
    avatar_rec[names[i]] = avatars[i]
for i in avatar_rec:
    img = Image.open(avatar_rec[i])
    imgplot = plt.imshow(img)
    plt.title(i)
    plt.show(block=False)
    plt.pause(3)
    plt.close()
    
#print (avatar_rec)
players=initialize(names,avatar_rec)

n = int(input("Enter the number of matches for each combination : "))
m = int(input("Enter the number of matches per day : "))

all_matches = []
for i in range(n):
    all_matches.extend(h2h)
#print(all_matches)
print("Generating Daily Schedule")
daily_schedule=generate_schedule(all_matches, m)

table = get_league_table()
