from typing import Union

from fastapi import FastAPI, HTTPException

from datetime import datetime

app = FastAPI()


@app.get("/dividir/{a}/{b}")
def sumar_service(a: int, b: int):
    if b == 0:
        raise HTTPException(
            status_code=400,
            detail="El divisor no puede ser cero"
        )
    return {"division": a / b}

@app.get("/getDate")
def date_service():
    return {"La fecha es": datetime.now().strftime("%Y-%m-%d %H:%M:%S")  }