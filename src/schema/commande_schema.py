from pydantic import BaseModel
from datetime import date
from typing import Optional

class CommandeBaseSchema(BaseModel):
    
    codcli: int
    datcde : date
    nbcolis : Optional[int] = None
    barchive : Optional[int] = None
    bstock : Optional[int] = None
    timbrecli : Optional[int] = None
    timbrecde : Optional[int] = None
    cheqcli : Optional[int] = None
    cdeComt: Optional[int]= None


class CommandeCreateSchema(CommandeBaseSchema):
    
    pass

class CommandeUpdateSchema(CommandeBaseSchema):
    pass
    
class CommandeInDBSchema(CommandeBaseSchema):
    codcde : int 
   
    class Config():
        from_attributes = True
