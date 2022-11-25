from fastapi import APIRouter
from app.schemas import User,UserId,usuarios

router = APIRouter(
    prefix='/user',
    tags=['Users']
)
@router.get('/ruta1')
def ruta1():
    return {'mensaje':'Bienvenido'}

@router.get('/')
def Obtener_usuarios():
    return usuarios

@router.post('/')
def crear_usuario(user:User):
    usuario = user.dict()
    usuarios.append(usuario)
    return {'Respuesta':'Usuario creado satisfactoriamente!'}

@router.post('/{user_id}')
def obtener_usuario(user_id:int):
    for user in usuarios:
        if user['id'] == user_id:
            return {'usuario':user}
    return {'respuesta':'Usuario no encontrado!'}

@router.post('/obtener_usuario')
def obtener_usuario(user_id:UserId):
    for user in usuarios:
        if user['id'] == user_id.id:
            return {'usuario':user}
    return {'respuesta':'Usuario no encontrado!'}

@router.delete('/{user_id}')
def eliminar_usuario(user_id:int):
    for index,user in enumerate(usuarios):
        if user['id'] == user_id:
            usuarios.pop(index)
            return {'Respuesta':'Usuario eliminado correctamente!'}
    return {'Respuesta':'Usuario no encontrado!'}

@router.put('/{user_id}')
def actualizar_usuario(user_id:int,updateUser:User):
    for index,user in enumerate(usuarios):
        if user['id'] == user_id:
            usuarios[index]['id'] = updateUser.dict()['id']
            usuarios[index]['nombre'] = updateUser.dict()['nombre']
            usuarios[index]['apellido'] = updateUser.dict()['apellido']
            usuarios[index]['direccion'] = updateUser.dict()['direccion']
            usuarios[index]['telefono'] = updateUser.dict()['telefono']
            return {'Respuesta':'Usuario actualizado correctamente!'}
    return {'Respuesta':'Usuario no encontrado'}