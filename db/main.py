from fastapi import FastAPI
import asyncpg
import os

app = FastAPI()

DB_CONFIG = {
    "host": os.getenv("SENA_HOST"),  
    "port": 6543,
    "database": "postgres",
    "user": "postgres.wzlqnyidditqopwyxboh",
    "password": os.getenv("SENA_PWD"),
    "ssl": "require",
}

pool: asyncpg.Pool | None = None


@app.on_event("startup")
async def startup():
    global pool
    pool = await asyncpg.create_pool(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        database=DB_CONFIG["database"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        ssl=DB_CONFIG["ssl"],
        min_size=1,
        max_size=5
    )


@app.on_event("shutdown")
async def shutdown():
    await pool.close()


@app.get("/aprendices")
async def get_aprendices():
    async with pool.acquire() as conn:
        rows = await conn.fetch("""
            SELECT id, nombre, correo, edad
            FROM public.adso_nocturno;
        """)

        # asyncpg devuelve Record → convertir a dict
        return [dict(row) for row in rows]
