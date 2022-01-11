import requests
import json
head={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
#https://china.nba.com/schedule/#!/7
re=requests.get("https://china.nba.com/static/data/season/schedule_7.json",headers=head)
#print(re.text)
j=json.loads(re.text)
#print(len(j['payload']['dates'][0]['games']))
for i in range (len(j['payload']['dates'][0]['games'])):
    print(j['payload']['dates'][0]['games'][i]['awayTeam']['profile']['name'],":",j['payload']['dates'][0]['games'][i]['homeTeam']['profile']['name'])
    print(j['payload']['dates'][0]['games'][i]['boxscore']['awayScore'],":",j['payload']['dates'][0]['games'][i]['boxscore']['homeScore'])
