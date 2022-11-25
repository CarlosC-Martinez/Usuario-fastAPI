#Dos formas de ejecutar FastAPI

1. Terminal: 
    uvicorn main:app

2. agregar las lineas de codigo
    import uvicorn

    if __name__=="__main__":
        uvicorn.run("main:app",port=8000,reload=True) 

   Terminal:
    python main.py 