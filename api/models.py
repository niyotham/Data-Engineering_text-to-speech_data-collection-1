from pydantic import BaseModel
class AudioData(BaseModel):
    url: str
    id:str

    class Config:
        arbitrary_types_allowed = True