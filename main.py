import requests
import time

t = 908
while (True):
    payload = {'content': "!work"}

    header = {
        'authorization':
        "TOKEN"
    }

    r = requests.post(
        "https://discord.com/api/v9/channels/CHANNEL_ID/messages",
        json=payload,
        headers=header)
    print("sent")
    time.sleep(t)
 
