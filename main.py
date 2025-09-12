from fastapi import FastAPI
from pydantic import BaseModel

### creacion de la clase Item
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float

app = FastAPI()

## uso del parametro POST
@app.post("/api/v1/items/")
async def create_item(item: Item):
    return (f"El Item {item.name} es: {item.description}, cuesta {item.price} y tiene un impuesto de {item.tax}")

### este es un ENDPOINT
@app.get("/") 
async def hello_world():
    return "Hello world!"

### uso del parametro PATH
@app.get("/api/v1/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}