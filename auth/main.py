from fastapi import FastAPI, Depends, HTTPException, status
import models, database, security, schemas
from sqlalchemy.orm import Session
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash_password(password: str):
    return pwd_context.hash(password)

# Crea las tablas automáticamente al iniciar el contenedor
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Microservicio Base")

@app.get("/health")
def health_check():
    return {"status": "ok", "mensaje": "El servicio está vivo"}

@app.get("/ruta-protegida", dependencies=[Depends(security.verificar_token)])
def ruta_protegida():
    return {"mensaje": "¡Autenticación exitosa entre servicios!"}

@app.post("/registro", status_code=status.HTTP_201_CREATED)
def registrar_usuario(data: schemas.AuthCreate, db: Session = Depends(database.get_db)):
    # buscar si existe usuario con el mismo nombre:
    valido = db.query(models.Auth).filter(models.Auth.nombre == data.nombre).first()
    if valido is not None:
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El nombre de usuario ya esta en uso"
                )
    hashed_password = hash_password(data.password)
    nuevo_usuario = models.Auth(
            nombre=data.nombre,
            password=hashed_password
            )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    # TODO: returnar token
    return {
            "mensaje": "Usuario registrado con exito",
            "id":     f"id: {nuevo_usuario.id}",
            "nombre": f"nombre de usuario: {nuevo_usuario.nombre}"
            }

@app.post("/login", status_code=status.HTTP_200_OK)
def login(data: schemas.AuthLogin, db: Session = Depends(database.get_db)):
    # verificar si usuario no existe
    user_db = db.query(models.Auth).filter(models.Auth.nombre == data.nombre).first()
    if user_db is None:
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No existe un usuario con ese nombre"
                )
    hashed_password = hash_password(data.password)

    if user_db.password != hashed_password:
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Contrasena incorrecta"
                )

    # TODO: returnar token y mensaje de exito
    return {
            "mensaje": "Usuario logeado exitosamente",
            }

