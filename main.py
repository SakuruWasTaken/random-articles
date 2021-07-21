import os, sys, random, time, json, requests
from dhooks import Webhook, File

with open('config.json', 'r') as handle:
    config = json.load(handle)

interval = (config["interval"])
hook = Webhook((config["webhook"]))
my_string = "do you like "
index = my_string.find('like')

def eatfood():
    print ("Sending articles every " + str(interval) + " seconds.")
    while True:
        article = requests.get('https://en.wikipedia.org/w/api.php?action=query&format=json&list=random&rnnamespace=0&rnlimit=1').json()
        title = article['query']['random'][0]['title']
        content = my_string[:index] + my_string[index:] + title
        hook.send(content=content)
        print(content)
        time.sleep(int(interval))
eatfood();
