from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import tqdm
import re
import time,json
import os
def getavatars():
    html = urlopen('https://naqvi-tech.blogspot.com/2018/07/8-ball-pool-all-avatar-orignial-images_74.html')
    bs = BeautifulSoup(html, 'html.parser')
    images = bs.find_all('img', {'data-original-height':re.compile('\d'),'border':re.compile('0'),'src':re.compile('.jpg')})
    count = 1
    if(not os.path.exists('avatars')):
        os.mkdir('avatars')
    for image in tqdm.tqdm(images): 
        urlretrieve(image['src'],'avatars/{}.png'.format(count))
        count+=1

def initialize(names,avatar_rec):
    print("Initializing your data")
    players={}
    for i in tqdm.tqdm(names):
        players[i]={'wins':0, 'losses':0, 'draws':0, 'gs':0, 'gc':0, 'avatar':avatar_rec[i]}
        time.sleep(0.25)
    with open('records.json','w') as f:
        json.dump(players,f)
        return players
    return players

def generate_schedule(matches,m):
    day = 1
    daily_schedule={1:{}}
    import random
    random.shuffle(matches)
    for idx,i in enumerate(matches):
        daily_schedule[day][idx]={ "p1":i[0], "p2":i[1]}
        if (idx+1)%m==0:
            day+=1
            daily_schedule[day]={}
    with open("schedule.json","w") as f:
        json.dump(daily_schedule, f)
    return daily_schedule

def get_schedule():
    sched={}
    with open('schedule.json','r') as f:
        sched=json.load(f)
    return sched

def get_records():
    records={}
    with open('records.json','r') as f:
        records=json.load(f)
    return records

def get_league_table():
    import pandas as pd
    df = pd.read_json('records.json').transpose()
    df['Points']=df['wins']*3 + df['draws']
    df['Goal_diff']=df['gs'] - df['gc']
    df.sort_values(by=['Points','Goal_diff'], ascending=False, inplace=True)
    df = df[['Points','wins','draws','losses','gs','gc','Goal_diff']]
    print(df)
    return df

def generate_league_pdf():
    df=get_league_table()
    from jinja2 import Environment, FileSystemLoader
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("league-table.html")
    template_vars = {"title" : "Pes league-table",
                 "national_pivot_table": df.to_html()}
    html_out = template.render(template_vars)
    from weasyprint import HTML
    HTML(string=html_out).write_pdf("league-table.pdf",stylesheets=["style.css"])
    print(html_out)
if __name__=="__main__":
    generate_league_pdf()
