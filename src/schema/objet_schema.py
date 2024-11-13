from pydantic import BaseModel
from typing import Optional

class ObjetBaseSchema(BaseModel):
    libobj : Optional[str] = None
    tailleobj : Optional[str] = None
    puobj : Optional[float] = None
    poidsobj : Optional[float] = None
    indispobj : Optional[int] = None
    o_imp : Optional[int] = None
    o_aff : Optional[int] = None
    o_cartp : Optional[int] = None
    points : Optional[int] = None
    o_ordre_aff : Optional[int] = None

class ObjetCreateSchema(ObjetBaseSchema):
    libobj: str

class ObjetUpdateSchema(ObjetBaseSchema):
    pass
    
class ObjetInDBSchema(ObjetBaseSchema):
    codobj : int

    class Config():
        from_attributes = True

