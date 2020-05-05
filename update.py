from utils import *
import pprint
sched = get_schedule()
pprint.pprint(sched)
day = input("Enter day : ")
idx = input("Enter Match id :")
match = sched[day][idx]
print(f"{match['p1']} vs {match['p2']}")
score=[int(x) for x in input("Enter score : ").split("-")]
#print(score)
winner = None
if score[0]>score[1]:
    winner = match['p1']
elif score[1]>score[0]:
    winner = match['p2']

records = get_records()
if winner == None :
    records[match['p1']]['draws']+=1
    records[match['p2']]['draws']+=1
elif winner == match['p1']:
    records[match['p1']]['wins']+=1
    records[match['p2']]['losses']+=1
else:
    records[match['p2']]['wins']+=1
    records[match['p1']]['losses']+=1
records[match['p1']]['gs']+=score[0]
records[match['p2']]['gc']+=score[0]
records[match['p1']]['gc']+=score[1]
records[match['p2']]['gs']+=score[1]
import json
with open('records.json','w') as f:
    json.dump(records,f)
table=get_league_table()
generate_league_pdf()

