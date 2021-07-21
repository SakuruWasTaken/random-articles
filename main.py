import os, sys, random, time, json, requests
from dhooks import Webhook, File

with open('config.json', 'r') as handle:
    config = json.load(handle)

interval = (config["interval"])
hook = Webhook((config["webhook"]))
    
def eatfood():
    print ("Sending articles every " + str(interval) + " seconds.")
    while True:
        r = requests.get('https://en.wikipedia.org/w/api.php?action=query&format=json&list=random&rnnamespace=0&rnlimit=1')
        article = r.json()
        title = article['query']['random'][0]['title']
        my_string = 'do you like '
        index = my_string.find('like')
        final_string = my_string[:index] + my_string[index:] + title
        content = final_string
        hook.send(content=content)
        time.sleep(int(interval))
eatfood();
