from pydantic import BaseModel
from typing import Optional


class ClientBaseSchema(BaseModel):
    genrecli: str
    nomcli: str
    prenomcli: str
    adresse1cli: Optional[str] = None
    adresse2cli: Optional[str] = None
    adresse3cli: Optional[str] = None
    telcli: Optional[str] = None
    emailcli: Optional[str] = None
    portcli: Optional[str] = None
    newsletter: Optional[int] = None


class ClientCreateSchema(ClientBaseSchema):
    pass


class ClientInDBSchema(ClientBaseSchema):
    codcli: int

    class Config:
        from_attributes = True


class ClientUpdateSchema(ClientBaseSchema):
    genrecli: Optional[str] = None
    nomcli: Optional[str] = None
    prenomcli: Optional[str] = None
    adresse1cli: Optional[str] = None
    adresse2cli: Optional[str] = None
    adresse3cli: Optional[str] = None
    telcli: Optional[str] = None
    emailcli: Optional[str] = None
    portcli: Optional[str] = None
    newsletter: Optional[int] = None
