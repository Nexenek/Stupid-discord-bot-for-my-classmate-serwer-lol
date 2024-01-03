import requests
import time

t = 908
while (True):
    payload = {'content': "!work"}

    header = {
        'authorization':
        "TOKEN" #place your token here
    }

    r = requests.post(
        "https://discord.com/api/v9/channels/CHANNEL_ID/messages", #replace "CHANNEL_ID" with the actual channel ID
        json=payload,
        headers=header)
    print("sent")
    time.sleep(t)
 
