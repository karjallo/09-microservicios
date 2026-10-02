from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.orm import Session
import models, database, security, schemas

# Crea las tablas automáticamente al iniciar el contenedor
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Microservicio Base")

@app.get("/health")
def health_check():
    return {"status": "ok", "mensaje": "El servicio está vivo"}

@app.get("/items")
def get_item(id: int, nombre: str, db: Session = Depends(database.get_db)):
    busqueda = db.query(models.Catalog)
    # si existe nombre filtramos, sino hacemos return lista completa
    # ilike permite comodin en este caso %string% busca texto inicial, final o intermedio
    if nombre:
        busqueda = busqueda.filter(models.Catalog.nombre.ilike("f%{name}%"))
    # evitamos if id: para evitar imprecisiones cuando id = 0 -> false
    if id is not None:
        busqueda = busqueda.filter(models.Catalog.id == id)

    return busqueda

# TODO: tras crear un item nuevo, mandar a inventory para que coincidan ids
@app.post("/items", response_model=schemas.CatalogResponse)
def create_item(item: schemas.CatalogCreate, db: Session = Depends(database.get_db)):
    nuevo_item = models.Catalog(nombre=item.nombre, precio=item.precio)
    db.add(nuevo_item)
    db.commit()
    db.refresh(nuevo_item)
    return nuevo_item

# recibe id del producto y nombre, precio
@app.patch("/items/{id}", response_model=schemas.CatalogResponse)
def edit_item(id: int, item_data: schemas.CatalogUpdate, db: Session = Depends(database.get_db)):
    # buscar si existe el item en db con el id dado
    item_db = db.query(models.Catalog).filter(models.Catalog.id == id).first()
    if item_db is None:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"El item con id {id} no existe"
                )

    # actualizar solo los campos pasados
    if item_data.nombre is not None:
        item_db.nombre = item_data.nombre

    if item_data.precio is not None:
        item_db.precio = item_data.precio

    # commit cambios
    db.commit()
    db.refresh(item_db)

    return item_db

@app.put("/items/{id}", response_model=schemas.CatalogResponse)
def replace_item(id: int, item: schemas.CatalogReplace, db : Session = Depends(database.get_db)):
    # corroborar que exista
    item_db = db.query(models.Catalog).filter(models.Catalog.id == id).first()
    if item_db is None:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"El item con id {id} no existe"
                )

    # reemplazar el archivo
    item_db.nombre = item.nombre
    item_db.precio = item.precio

    # commit
    db.commit()
    db.refresh(item_db)

    return item_db

# TODO: tras eliminar una entrada en catalog, mandar a inventory para que se
# elimine tambien
@app.delete("/items/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(id: int, db : Session = Depends(database.get_db)):
    # corroborar que exista
    item_db = db.query(models.Catalog).filter(models.Catalog.id == id).first()
    if item_db is None:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"El item con id {id} no existe"
                )

    # commit
    db.delete(item_db)
    db.commit()




