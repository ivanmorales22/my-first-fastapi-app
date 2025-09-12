from fastapi import FastAPI

app = FastAPI()

### este es un ENDPOINT
@app.get("/") 
async def hello_world():
    return "Hello world!"
