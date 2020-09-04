import json

def loadSubscribers():
    fp = open("./data/subscribers.json", "r")
    return json.load(fp)