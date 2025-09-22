# Simulacion de bases de datos sin base de datos ni servidor :) jajaja

usuarios = [
    {"id": 1, "nombre": "Ana", "email": "ana@email.com"},
    {"id": 2, "nombre": "Luis", "email": "luis@email.com"}
]

def get_user():
    return usuarios

def post_user(usuario):
    usuarios.append(usuario)
    return {"message": "Usuario agregado", "usuario": usuario}

def put_user(id,dato):
    for user in usuarios:
        if user["id"] == id:
            user.update(dato)
            return {"message":"Usuario editado","usuario":user}
    return {"error":"Usuario no encontrado"}

def delete_user(id):
    for user in usuarios:
        if user["id"]==id:
            usuarios.remove(user)
            return {"message":"Usuario eliminado"}
    return {"error":"Usuario no encontrado"}

print("Crear usuario",post_user({"id": 3, "nombre": "Sofía", "email": "sofia@email.com"}))
print("Editar usuario",put_user(2,{"nombre":"jose"}))
print("Eliminar usuario", delete_user(1))
print("Usuarios: ", get_user())