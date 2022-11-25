from pydantic import BaseModel
from typing import Optional
from datetime import datetime

#User Model
class User(BaseModel):
    id:int
    nombre:str
    apellido:str
    direccion:Optional[str]
    telefono:int
    correo:str
    creacion:datetime = datetime.now()

class UserId(BaseModel):
    id:int

usuarios = [
  {
  "id": 0,
  "nombre": "string",
  "apellido": "string",
  "direccion": "string",
  "telefono": 0,
  "correo":"aaa",
  "creacion": "2022-11-13T19:22:04.020942"
},
{
  "id": 1,
  "nombre": "string",
  "apellido": "string",
  "direccion": "string",
  "telefono": 0,
  "correo":"aaa",
  "creacion": "2022-11-13T19:22:04.020942"
}]