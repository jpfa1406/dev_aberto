import requests
from datetime import date
from babel.dates import format_date


def hello():
    c = requests.get('https://api.github.com/repos/insper/dev-aberto/commits')
    info = c.json()
    commit_info = info[0]['commit']['author']
    data = (commit_info['date']).split('T')[0].split('-')
    for i in range(len(data)):
        data[i] = int(data[i])
    d = date(data[0], data[1], data[2])
    return format_date(d), commit_info['name']
