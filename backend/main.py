from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend funcionando con VS Code y venv!"}
