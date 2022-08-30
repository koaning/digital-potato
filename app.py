from fastapi import FastAPI, Response
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/", StaticFiles(directory="public", html = True))

@app.get("/api/")
def api(response: Response):
    return {"message": "this api works"}
