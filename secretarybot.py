import requests
import json
import time
import datetime
import pandas as pd
import numpy as np


sheet_id = '1y970ypoavFkM1zgtWkn6qZ7YsvnCJdxFvKLOZOUU_ac'
sheet_name = 'events'


# TODO: uploads logo
# data = open('./byxlogo.png', 'rb').read()
# res = requests.post(url='https://image.groupme.com/pictures',
#                     data=data,
#                     headers={'Content-Type': 'image/png',
#                              'X-Access-Token': 'rLuheSG4Swp8V0rWCOGA4uIHDQzoHabwKPrmDW9a'})
# print(res.content)

# sends http post
def alert(event_name, event_type, event_date, event_time, distance, location):

    if event_type == np.nan:
        event_type = ''
    if distance == 3:
        message = 'Our ' + event_name + ' ' + event_type + ' is one month away on ' + event_date + '.'
    if distance == 2:
        message = 'We are one week away from the ' + event_name + ' ' + event_type + '.'
    if distance == 1:
        message = 'Our ' + event_name + ' ' + event_type + ' is TOMORROW'
        if event_time != np.nan:
            message += ' at ' + event_time
        if location != np.nan:
            message += ' at ' + location
        message += '.'
    print(message)

    res = requests.post(url='https://api.groupme.com/v3/bots/post',
                        data=json.dumps({'bot_id': 'cfe247bb3de3894f0f2d24c485', 'text': message}),
                        headers={'Content-Type': 'application/json'})
    print(res.text)


# dataframe from google sheet
def gather_events():
    url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
    df = pd.read_csv(url, parse_dates=['Event Date'])
    return df


# function to be run once a day
def sentinel():
    now = datetime.date.today()
    events = gather_events()
    for tuple in events.iterrows():
        event = tuple[1]
        dist = (event['Event Date'].date() - now).days
        dist = 1 if dist == 1 else 2 if dist == 7 else 3 if dist == 30 else 0
        if dist in [1, 2, 3]:
            alert(event['Event Name'], event['Event Type'], event['Event Date'].date().strftime("%m/%d/%Y"),
                  event['Event Time'], dist, event['Location'])

if __name__ == '__main__':
    sentinel()