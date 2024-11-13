from pydantic import BaseModel

class DetailBaseSchema(BaseModel):
    commentaire: str
    codcde : int
    qte : int
    colis : int
 
    
class DetailCreateSchema(DetailBaseSchema):
    pass
    
class DetailInDBSchema(DetailBaseSchema):
    id: int
    
    
    
    class Config():
        from_attributes = True
