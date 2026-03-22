from fastapi import APIRouter, HTTPException
from app.database import get_mysql_connection
from app.schemas import PacienteCreate, PacienteUpdate, PacienteResponse
from typing import List

router = APIRouter()

# Rutas para pacientes en metodos CRUD

# metodo GET para obtener todos los pacientes
@router.get("/pacientes", response_model=List[PacienteResponse])
def get_pacientes():
    conn = get_mysql_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM pacientes")
            return cursor.fetchall()
    finally:
        conn.close()

# metodo GET para obtener un paciente por ID
@router.get("/pacientes/{id}", response_model=PacienteResponse)
def get_paciente(id: int):
    conn = get_mysql_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM pacientes WHERE id_paciente = %s", (id,))
            paciente = cursor.fetchone()
            if not paciente:
                raise HTTPException(status_code=404, detail="Paciente no encontrado")
            return paciente
    finally:
        conn.close()
# metodo POST para crear un nuevo paciente
@router.post("/pacientes", response_model=PacienteResponse)
def create_paciente(paciente: PacienteCreate):
    conn = get_mysql_connection()
    try:
        with conn.cursor() as cursor:
            sql = """INSERT INTO pacientes 
                     (nombre, apellido, fecha_nacimiento, sexo, telefono, correo, id_diagnostico)
                     VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (
                paciente.nombre, paciente.apellido,
                paciente.fecha_nacimiento, paciente.sexo,
                paciente.telefono, paciente.correo,
                paciente.id_diagnostico
            ))
            conn.commit()
            cursor.execute("SELECT * FROM pacientes WHERE id_paciente = %s", (cursor.lastrowid,))
            return cursor.fetchone()
    finally:
        conn.close()

# metodo PUT para actualizar un paciente existente
@router.put("/pacientes/{id}", response_model=PacienteResponse)
def update_paciente(id: int, paciente: PacienteUpdate):
    conn = get_mysql_connection()
    try:
        with conn.cursor() as cursor:
            fields = {k: v for k, v in paciente.dict().items() if v is not None}
            if not fields:
                raise HTTPException(status_code=400, detail="No hay datos para actualizar")
            set_clause = ", ".join([f"{k} = %s" for k in fields])
            sql = f"UPDATE pacientes SET {set_clause} WHERE id_paciente = %s"
            cursor.execute(sql, (*fields.values(), id))
            conn.commit()
            cursor.execute("SELECT * FROM pacientes WHERE id_paciente = %s", (id,))
            return cursor.fetchone()
    finally:
        conn.close()

# metodo DELETE para eliminar un paciente por ID
@router.delete("/pacientes/{id}")
def delete_paciente(id: int):
    conn = get_mysql_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM pacientes WHERE id_paciente = %s", (id,))
            conn.commit()
            return {"mensaje": "Paciente eliminado correctamente"}
    finally:
        conn.close()
        
# metodo PATCH para actualizar parcialmente un paciente
@router.patch("/pacientes/{id}", response_model=PacienteResponse)
def patch_paciente(id: int, paciente: PacienteUpdate):
    conn = get_mysql_connection()
    try:
        with conn.cursor() as cursor:
            fields = {k: v for k, v in paciente.dict().items() if v is not None}
            if not fields:
                raise HTTPException(status_code=400, detail="No hay datos para actualizar")
            set_clause = ", ".join([f"{k} = %s" for k in fields])
            sql = f"UPDATE pacientes SET {set_clause} WHERE id_paciente = %s"
            cursor.execute(sql, (*fields.values(), id))
            conn.commit()
            cursor.execute("SELECT * FROM pacientes WHERE id_paciente = %s", (id,))
            return cursor.fetchone()
    finally:
        conn.close()