from pydantic import BaseModel


class ClientBaseSchema(BaseModel):
    prenomcli: str
    nomcli: str


class ClientInDBSchema(ClientBaseSchema):
    codcli: int
    genrecli: str
    adresse1cli: str
    adresse2cli: str
    adresse3cli: str
    villecli_id: int
    telcli: str
    emailcli: str
    portcli: str
    newsletter: int
