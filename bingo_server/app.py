from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Bingo server is up and running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "bingo_server.app:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )