from pydantic import BaseModel
from typing import Optional


class DetailBaseSchema(BaseModel):
    commentaire: Optional[str] = None
    codcde: int
    qte: int
    colis: int


class DetailCreateSchema(DetailBaseSchema):
    pass


class DetailUpdateSchema(DetailBaseSchema):
    commentaire: Optional[str] = None
    codcde: Optional[int] = None
    qte: Optional[int] = None
    colis: Optional[int] = None


class DetailInDBSchema(DetailBaseSchema):
    id: int

    class Config:
        from_attributes = True
