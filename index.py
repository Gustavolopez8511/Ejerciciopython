import sqlite3

conexion = sqlite3.connect('ejemplo.db')

# Creamos el cursor
cursor = conexion.cursor()

# Ahora crearemos una tabla de usuarios para almacenar nombres, edades y emails
#cursor.execute("CREATE TABLE Estudiante (id VARCHAR(10),nombre VARCHAR(100), apellido VARCHAR(100), cedula VARCHAR(30), telefono INTEGER)")

#cursor.execute("INSERT INTO Estudiante VALUES ('01','Julio','casas','12345678',2222222)")

#cursor.execute("SELECT * FROM Estudiante")
#Estudiante = cursor.fetchone()
#print(Estudiante[2])
#Estudiante = cursor.fetchone()

#Estudiante = [
    #('01','Julio','casas','12345678',2222222),
    #('02','carlos','restrepo','88888888',2333333),
    #('03','natalia','rua','12999999',2444444),
    #('04','nando','hernandez','1111111111',2555555),
    #('05','julieta','perez','19191919',2666666),
#]
#cursor.executemany("INSERT INTO Estudiante VALUES (?,?,?,?,?)", Estudiante)

cursor.execute("SELECT * FROM Estudiante")
Estudiante = cursor.fetchall()
for Estudiante in Estudiante:
    print(Estudiante)
# Guardamos los cambios haciendo un commit
conexion.commit()

conexion.close()