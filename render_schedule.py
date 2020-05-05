from utils import *

sched = get_schedule()
for i in sched.keys():
    print("DAY-{}".format(i))
    day = sched[i]
    print("      MatchID        P1vsP2")
    for matchid in day:
        match = day[matchid]
        print(f"        {matchid}        {match['p1']} vs {match['p2']}")



