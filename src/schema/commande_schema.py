from pydantic import BaseModel
from datetime import date

class CommandeBaseSchema(BaseModel):
    codcli: int
    codcde : int 
    nbcolis : int
    barchive : int
    bstock : int
    timbrecli : float
    timbrecde : float
    cheqcli : float
    datcde : date
    


class CommandeCreateSchema(CommandeBaseSchema):
    pass
    
class CommandeInDBSchema(CommandeBaseSchema):
    cdeComt: str
   
    class Config():
        from_attributes = True
