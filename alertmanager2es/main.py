import os
from datetime import date,datetime
from fastapi import Body, FastAPI
import requests
import json

es_host = os.getenv('ES_HOST','es-gcp.kiwisns.com')
es_port = os.getenv('ES_PORT','9200')
es_url = "http://" + es_host + ":" + es_port
index = "alertmanager-email" + "-" + date.today().strftime("%Y-%m-%d")

# timestamp = datetime.timestamp(datetime.now())
# print(timestamp)
# # time = datetime.fromtimestamp(timestamp)
# time = datetime.isoformat(datetime.fromtimestamp(timestamp))
# print(time)

app = FastAPI()
@app.post("/alert")
async def update_item( email: dict = Body(...)):
    msg = email
    timestamp = datetime.timestamp(datetime.now())
    alerts = msg["alerts"]
    for alert in alerts:
        print(timestamp)
        alert["timestamp"] = datetime.isoformat(datetime.utcfromtimestamp(timestamp))
        print(alert["timestamp"])
        r = requests.post(es_url + "/" + index + "/_doc/?pretty",data=json.dumps(alert),headers={'Content-Type': 'application/x-ndjson'})
        text = r.content
        respone = r.headers
        print(text,respone,alert)
    return text
