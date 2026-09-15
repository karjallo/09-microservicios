from fastapi import FastAPI, Depends
import models, database, security

# Crea las tablas automáticamente al iniciar el contenedor
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Microservicio Base")

@app.get("/health")
def health_check():
    return {"status": "ok", "mensaje": "El servicio está vivo"}

@app.get("/ruta-protegida", dependencies=[Depends(security.verificar_token)])
def ruta_protegida():
    return {"mensaje": "¡Autenticación exitosa entre servicios!"}