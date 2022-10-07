from pydantic import BaseModel
class AudioData(BaseModel):
    base64: str
    id:str

    class Config:
        arbitrary_types_allowed = True