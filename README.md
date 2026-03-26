"# backendpacientes" 
router = APIRouter() 
    //APIRouter permite separar las rutas en archivos y hacer el código más escalable.

conn = get_mysql_connection()
    //cada endpoint abre la conexion a la bd

conn.close()
    //cierra la conexion
        //¿Qué pasa si no cierras la conexión? Se pueden saturar las conexiones a la base de datos y afectar el rendimiento.

with conn.cursor() as cursor:
    //el objeto que recorre fila por fila
        //ejecuta consultas SQL
        //porque usar with? para que se maneje automaticamente los recursos y evitar fugas de memoria

cursorclass=pymysql.cursors.DictCursor
    //hace los resultados en diccionarios y no en tuplas
        //sirve para convertir los datos en json en FastAPI

cursor.fetchall() vs fetchone()
  fetchall() // trae todos los registros
  fetchone()  //trae solo un registro

if not paciente:
    raise HTTPException(status_code=404, detail="Paciente no encontrado")
        //lanza error si no existe

response_model=PacienteResponse
    //sirve para que la respuesta tenga la estructura correcta

fields = {k: v for k, v in paciente.dict().items() if v is not None}
    //toma todo los campos enviados e ignora los none
    //sirve para actualizar los campos que el usuario manda, en especial en PATCH

set_clause = ", ".join([f"{k} = %s" for k in fields])
    // es seguro porque los valores pasan como paramentros evitando inyecciones SQL
    //no hace que se trate como dato y no como codigo

cursor.execute(sql, (...)) // evita SQL injection

cursor.lastrowid  
    // se usa para devolver el registro recien creado

conn.commit() // guarda cambios en la db


allow_origins=["*"] // permite acceso desde el frontend
