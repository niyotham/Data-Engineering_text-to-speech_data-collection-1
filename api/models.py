from pydantic import BaseModel
from fastapi import File, UploadFile
class AudioData(BaseModel):
    id:str
    audio:UploadFile= File()
    class Config:
        arbitrary_types_allowed = True