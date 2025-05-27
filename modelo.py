import peewee as pw
import pymysql
pymysql.install_as_MySQLdb()

# Conexión a la base de datos SQLite
farmacia_ujat = pw.SqliteDatabase('farmacia_ujat.db')

# Definir la tabla 'farmaco'
class Farmaco(pw.Model):
    nombre = pw.CharField(max_length=255, primary_key=True)
    descripcion = pw.TextField()
    categoria = pw.CharField(max_length=255, null=True)
    interacciones = pw.TextField(null=True)

    class Meta:
        database = farmacia_ujat
        table_name = 'farmaco'

# Definir la tabla 'medicamento'
class Medicamento(pw.Model):
    id = pw.AutoField()
    clave = pw.CharField(max_length=255)
    descripcion = pw.CharField(max_length=255)
    presentacion = pw.CharField(max_length=255)
    clasificacion = pw.CharField(max_length=255)
    nivel_atencion = pw.CharField(max_length=255)
    nombre_farmaco = pw.ForeignKeyField(
        Farmaco,
        backref='medicamentos',
        column_name='nombre_farmaco',
        field='nombre',
        null=True
    )

    class Meta:
        database = farmacia_ujat
        table_name = 'medicamento'  # Puedes definir nombre si quieres

farmacia_ujat.connect()
