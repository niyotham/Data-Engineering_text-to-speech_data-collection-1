from fastapi import FastAPI, File, UploadFile
# import boto3
import producer
import consumer
app = FastAPI()

app.add_middleware(
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/check")
def check():
    return "Your API is up!"

@app.get("/loadText")
def get_text():

    # Set file path
    pass

@app.post("/send")
def send_audio():

    pass