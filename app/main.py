import uvicorn
from fastapi import FastAPI



app = FastAPI(
    title='OpenTour',
    version='1.0'
)



@app.get("/")
async def mainpage():
    return {"is_working": True}



if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        reload=True, 
        host='localhost', 
        port=8000
        )
