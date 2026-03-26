from fastapi import APIRouter, HTTPException
from app.database import get_mysql_connection
from app.schemas import PacienteResponse, ConsultaResponse
from typing import List

router = APIRouter()

# GET todos los pacientes
@router.get("/pacientes", response_model=List[PacienteResponse])
def get_pacientes():
    conn = get_mysql_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM pacientes")
            return cursor.fetchall()
    finally:
        conn.close()

# GET un paciente por ID
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

# GET todas las consultas
@router.get("/consultas", response_model=List[ConsultaResponse])
def get_consultas():
    conn = get_mysql_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM consultas")
            return cursor.fetchall()
    finally:
        conn.close()

# GET una consulta por ID
@router.get("/consultas/{id}", response_model=ConsultaResponse)
def get_consulta(id: int):
    conn = get_mysql_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM consultas WHERE id_consulta = %s", (id,))
            consulta = cursor.fetchone()
            if not consulta:
                raise HTTPException(status_code=404, detail="Consulta no encontrada")
            return consulta
    finally:
        conn.close()