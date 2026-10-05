# TODO: actualizar par aque refleje order
from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.orm import Session
import models, database, security, schemas

# Crea las tablas automáticamente al iniciar el contenedor
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Microservicio Base")

@app.get("/health")
def health_check():
    return {"status": "ok", "mensaje": "El servicio está vivo"}

# TODO: brinda los pedidos realizados por el usuario
@app.get("/pedidos")
def get_item(id: int | None, db: Session = Depends(database.get_db)):
    busqueda = db.query(models.Pedidos)
    # si existe nombre filtramos, sino hacemos return lista completa
    # evitamos if id: para evitar imprecisiones cuando id = 0 -> false
    if id is not None:
        busqueda = busqueda.filter(models.Pedidos.id == id)

    return busqueda.all()

# TODO: post endpoint para crear pedido con id de producto

# recibe id y otro int pudiendo ser este negativo, para realizar cambios
@app.patch("/pedidos/{id}", response_model=schemas.PedidosResponse)
def edit_item(id: int, delta: int, db: Session = Depends(database.get_db)):
    # buscar si existe el item en db con el id dado
    item_db = db.query(models.Pedidos).filter(models.Pedidos.id == id).first()
    if item_db is None:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"El item con id {id} no existe"
                )

    item_db.cantidad = item_db.cantidad + delta

    # commit cambios
    db.commit()
    db.refresh(item_db)

    return item_db

# actualiza cantidades (reemplaza)
@app.put("/pedidos/{id}", response_model=schemas.PedidosResponse)
def replace_item(id: int, cantidad: int, db : Session = Depends(database.get_db)):
    # corroborar que exista
    item_db = db.query(models.Pedidos).filter(models.Pedidos.id == id).first()
    if item_db is None:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"El item con id {id} no existe"
                )

    # reemplazar el archivo
    item_db.cantidad = cantidad

    # commit
    db.commit()
    db.refresh(item_db)

    return item_db

# TODO: tras eliminar una entrada en catalog, mandar a inventory para que se
# elimine tambien
@app.delete("/pedidos/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(id: int, db : Session = Depends(database.get_db)):
    # corroborar que exista
    item_db = db.query(models.Pedidos).filter(models.Pedidos.id == id).first()
    if item_db is None:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"El item con id {id} no existe"
                )

    # commit
    db.delete(item_db)
    db.commit()




