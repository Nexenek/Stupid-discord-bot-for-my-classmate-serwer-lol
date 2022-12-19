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
        "https://discord.com/api/v9/channels/1054044541201686538/messages",
        json=payload,
        headers=header)
    print("wyslalem")
    time.sleep(t)
    #1054044541201686538
