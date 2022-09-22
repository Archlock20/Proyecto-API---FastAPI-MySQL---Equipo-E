from fastapi import APIRouter, Response, status
from config.db import conn
from models.user import users
from schemas.user import User
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT

key = Fernet.generate_key()
f = Fernet(key)

user = APIRouter()

# Ruta raiz, en donde se enlistan los estudiantes almacenados en la base de datos
@user.get("/users/lista_est", response_model=list[User], tags=["users"])
def get_liststudents():
    return conn.execute(users.select()).fetchall()


# Ruta y funcion para crear usuarios
@user.post("/users/add_est", response_model=User, tags=["users"])
def create_student(user: User):
    new_user = {"cedula": user.cedula, "name": user.name, "lastname": user.lastname,
                "age": user.age, "email": user.email, "gender": user.gender}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    result = conn.execute(users.insert().values(new_user))
    print(result)
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()


# Ruta y funcion para consultar usuarios a traves de su ID
@user.get("/users/search_est/{id}", response_model=User, tags=["users"])
def get_studentid(id: str):
    return conn.execute(users.select().where(users.c.id == id)).first()


# Ruta y funcion para consultar usuarios a traves de su numero de cedula
@user.get("/users/search_est_ced/{cedula}", tags=["users"])
def get_studentcedula(cedula: str):
    return conn.execute(users.select().where(users.c.cedula == cedula)).first()

# Ruta y funcion para consultar usuarios a traves de su numero de apellido/os
@user.get("/user/search_est_apellido/{lastname}", tags=["users"])
def get_studentapellido(lastname: str):
    return conn.execute(users.select().where(users.c.lastname == lastname)).first()


# Ruta y funcion para eliminar usuarios a traves de su ID
@user.delete("/users/delete_est/{id}", status_code=HTTP_204_NO_CONTENT, tags=["users"])
def delete_student(id: str):
    conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


# Ruta y funcion para la actualizacion de los datos de los estudiantes
@user.put("/users/update_est/{id}", response_model = User, tags=["users"])
def modify_student(id: str, user: User):
    conn.execute(users.update().values(cedula=user.cedula, name=user.name, lastname=user.lastname,
                 age=user.age, email=user.email, gender=user.gender, 
                 password=f.encrypt(user.password.encode("utf-8"))).where(users.c.id == id))
    return conn.execute(users.select().where(users.c.id == id)).first()
