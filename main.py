from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "서버 작동중"}
@app.post("/analyze")
def analyze():
    return {"result": "분석중"}
