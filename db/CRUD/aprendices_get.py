from database import pool,Router
from fastapi import HTTPException



@Router.get("/aprendices")
async def get_aprendices():
    async with pool.acquire() as conn:
        rows = await conn.fetch("""
            SELECT id, nombre, correo, edad
            FROM public.adso_nocturno;
        """)

        # asyncpg devuelve Record → convertir a dict
        return [dict(row) for row in rows]


@Router.get("/aprendices/{id}")
async def get_apendiz_by_id(id: int):
    async with pool.acquire() as conn:
        row = await conn.fetchrow("""
            SELECT id, nombre, correo, edad
            FROM public.adso_nocturno
            WHERE id = $1;
        """, id)

        if not row:
            raise HTTPException(status_code=404, detail="Aprendiz no encontrado")

        return dict(row)