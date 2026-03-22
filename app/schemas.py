from pydantic import BaseModel
from typing import Optional
from datetime import date

class PacienteCreate(BaseModel):
    nombre: str
    apellido: str
    fecha_nacimiento: date
    sexo: str
    telefono: str
    correo: str
    id_diagnostico: int

class PacienteUpdate(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    sexo: Optional[str] = None
    telefono: Optional[str] = None
    correo: Optional[str] = None
    id_diagnostico: Optional[int] = None

class PacienteResponse(BaseModel):
    id_paciente: int
    nombre: str
    apellido: str
    fecha_nacimiento: date
    sexo: str
    telefono: str
    correo: str
    id_diagnostico: int