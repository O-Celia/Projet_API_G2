from pydantic import BaseModel, Field
from typing import Optional

class ObjetBaseSchema(BaseModel):
    libobj : Optional[str] = Field(None, max_length=50) # Optionnel et limité à 50 caractères
    tailleobj : Optional[str] = Field(None, max_length=50) 
    puobj : Optional[float] = None
    poidsobj : Optional[float] = None
    indispobj : Optional[int] = None
    o_imp : Optional[int] = None
    o_aff : Optional[int] = None
    o_cartp : Optional[int] = None
    points : Optional[int] = None
    o_ordre_aff : Optional[int] = None

class ObjetCreateSchema(ObjetBaseSchema):
    
    libobj: str = Field(..., max_length=50) # Obligatoire et limité à 50 caractères

class ObjetUpdateSchema(ObjetBaseSchema):
    pass
    
class ObjetInDBSchema(ObjetBaseSchema):
    codobj : int

    class Config():
        from_attributes = True

