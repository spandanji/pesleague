from utils import *
import pandas as pd
import numpy as np
import pprint
sched = get_schedule()
extra_key = str(max([int(x) for x in sched.keys()]))
del sched[extra_key]

html_str=''
for i in sched:
    df = pd.DataFrame.from_dict(sched[i]).transpose()
    df.index.name="Match-ID"
    df.columns=['Player 1', 'Player 2']
    html_str+="<h2>Day {}</h2>".format(i)+"\n"+ df.to_html() + "\n\n"


from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("matches.html")
template_vars = {"title" : "Matchups",
                 "national_pivot_table": html_str}
html_out = template.render(template_vars)
from weasyprint import HTML
HTML(string=html_out).write_pdf("matchups.pdf",stylesheets=["style.css"])
