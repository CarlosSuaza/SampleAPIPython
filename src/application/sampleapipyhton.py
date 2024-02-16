
# sampleapipyhton:

from fastapi import FastAPI

app: FastAPI = FastAPI(
    title="Sample API Python",
    description="USBTCA202401"
)

@app.get("/sampleAPIPython",
    summary="Sample API Python",
    tags=["SampleAPIPython"])
async def operacion_get(dato_entrada: str):
    return dato_entrada