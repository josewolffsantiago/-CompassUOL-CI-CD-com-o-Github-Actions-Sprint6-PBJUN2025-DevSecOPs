from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World from docker hello-app:e68512a77a85774b4f630ba0844be6140030e356"}
