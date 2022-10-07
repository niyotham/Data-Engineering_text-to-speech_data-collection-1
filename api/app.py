import json
from urllib.request import Request
from fastapi import FastAPI, File, UploadFile,Request
from fastapi.middleware.cors import CORSMiddleware
import uuid
# import boto3
import pandas as pd
import producer
import consumer
import topic
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

path="/home/data/raw_data.csv"
@app.get("/check")
def check():
    return "Your API is up!"

@app.get("/loadText")
def get_text(request:Request):
    # Set file path
    df = pd.read_csv(path)
    text = df.sample()['headline']
    id=get_id(request)
    text['id']=id.replace("-",'')
    text.reset_index(drop=True,inplace=True)

    producer.produce(topic='g1-text',message=text.to_json())

    return(text)

@app.post("/send")
def send_audio():

    pass

def get_id(request):
    ip = request.client.host
    return f"{str(uuid.uuid4()).replace('-','')}-{ip.replace('.','')}"