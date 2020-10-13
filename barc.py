import requests
from bs4 import BeautifulSoup
import json

def ask_genre():
    response = requests.get('https://www.barcindia.co.in/data-insights')
    soup = BeautifulSoup(response.content,'html.parser')

    drop_down = soup.find_all('select')[1]
    options = [i.text for i in drop_down.find_all('option')]
    options = {i+1:options[i] for i in range(len(options))}

    for key,value in options.items():
        print(key,value)

    num = int(input("Select one of them: "))
    genre = options[num]
    return genre

genre = ask_genre()
url = 'https://www.barcindia.co.in/data-insights/filterChannel'
form_data = {"genre_cat_id":genre}

response = requests.post(url, data=form_data)
my_json = json.loads(response.text)

channels = my_json['obj_channels']
channels = {i['rank']:i['channels'] for i in channels}

print('\n','-'*40,'\n')
for rank,channel in channels.items():
    print(rank,channel)
print('\n','-'*40,'\n')    
