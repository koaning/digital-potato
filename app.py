from fastapi import FastAPI, Response
from fastapi.staticfiles import StaticFiles

app = FastAPI()


@app.get("/api/")
def api(response: Response):
    return {"message": "this api works"}

# It's a funny thing, but the order matters here.
app.mount("/", StaticFiles(directory="public", html = True))