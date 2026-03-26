from pydantic import BaseModel
from typing import Optional
from datetime import date

class PacienteResponse(BaseModel):
    id_paciente: int
    nombre: str
    apellido: str
    fecha_nacimiento: date
    sexo: str
    telefono: str
    correo: str
    id_diagnostico: int

class ConsultaResponse(BaseModel):
    id_consulta: int
    id_paciente: int
    fecha_consulta: date
    motivo: str
    diagnostico: str
    tratamiento: str