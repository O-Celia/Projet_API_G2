from pydantic import BaseModel

class ClientBaseSchema(BaseModel):
    prenom: str
    nom: str
    
class ClientInDBSchema(ClientBaseSchema):
    id: int