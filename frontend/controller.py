import sqlite3 as sql

def createDB():
    conn = sql.connect("insects.db")
    conn.commit()
    conn.close()

def createTableUsers():
    conn = sql.connect("insects.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE users (
            nombreUsuario text not null,
            password text not null,
            primary key(nombreUsuario)
        )"""
    )
    conn.commit()
    conn.close()

def createTableInsects():
    conn = sql.connect("insects.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE insects (
            nombreComun text not null,
            nombreCientifico text,
            divisionTaxonomica text,
            color text,
            primary key(nombreComun)
        )"""
    )
    conn.commit()
    conn.close()

def createTableInferencia():
    conn = sql.connect("insects.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE inferencias (
            nombreComun text not null,
            latitud float,
            longitud float,
            color text,
            nombreUsuario text,
            publico Integer
        )"""
    )
    conn.commit()
    conn.close()

def createTableBiblioteca():
    conn = sql.connect("insects.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE biblioteca (
            nombreComun text,
            detalles text,
            rutaImagen text
        )"""
    )
    conn.commit()
    conn.close()

def createTableBlog():
    conn = sql.connect("insects.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE blog (
            nombreUsuario text,
            comentario text,
            rutaImagen text
        )"""
    )
    conn.commit()
    conn.close()

def insertUser(nombreUsuario,password):
    conn = sql.connect("insects.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO users VALUES ('{nombreUsuario}','{password}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def insertRowInsects(nombreComun,nombreCientifico,divisionTaxonomica,color):
    conn = sql.connect("insects.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO insects VALUES ('{nombreComun}','{nombreCientifico}','{divisionTaxonomica}','{color}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def insertRowInferencia(nombreComun,latitud,longitud,color,nombreUsuario, publico):
    conn = sql.connect("insects.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO inferencias VALUES ('{nombreComun}',{latitud},{longitud},'{color}','{nombreUsuario}',{publico})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def readRowsInferencia():
    conn = sql.connect("insects.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM inferencias"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos

def searchUsers(nameUser, passw):
    conn = sql.connect("insects.db")
    cursor = conn.cursor()
    cursor2 = conn.cursor()
    instruccion = f"SELECT * FROM users WHERE nombreUsuario like ('{nameUser}')"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    if datos:
        if str(datos[0][1])== passw:
            message = ("WELCOME "+datos[0][0])
            loggin = True
        else:
            message = ("PASSWORD INCORRECTO "+datos[0][0])
            loggin = False
    else:
        message = ("EL USUARIO NO EXISTE")
        loggin = False
    conn.commit()
    conn.close()
    return loggin, message

def searchInsects(nombreComun):
    conn = sql.connect("insects.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM insects WHERE nombreComun like ('{nombreComun}')"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos

def deleteInsects(nombreComun):
    conn = sql.connect("insects.db")
    cursor = conn.cursor()
    instruccion = f"DELETE FROM insects WHERE nombreComun = ('{nombreComun}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def deleteInferencia(nombreComun):
    conn = sql.connect("insects.db")
    cursor = conn.cursor()
    instruccion = f"DELETE FROM inferencias WHERE nombreComun = ('{nombreComun}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def get_all_blogs():
    conn = sql.connect("insects.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM blog')
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    return data

def insertRowBlog(nombreUsuario,comentario,rutaImagen):
    conn = sql.connect("insects.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO blog VALUES ('{nombreUsuario}','{comentario}','{rutaImagen}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    #createDB()
    #createTableUsers()
    #createTableInsects()
    #createTableInferencia()
    #createTableBiblioteca()
    #createTableBlog()

    #insertUser("jalarcon","12345")
    #insertUser("grivera","54321")
    
    #insertRowInsects("Butterfly", "Lepidopteros", "Diurnas (Rophalocero), Nocturnas (Heterocero)", "#ffaa00")
    #insertRowInsects("Dragonfly", "Anisopteros", "Zygoptera, Epiprocta", "#0066ff")
    #insertRowInsects("Grasshopper", "Orthoptera Caelifera", "Tridactyloidea,Tetrigoidea, Eumastacidae, Proscopiidae, Pneumoridae, Pyrgomorphidae, Acrididae + Pamphagidae", "#00ff11")
    #insertRowInsects("Ladybird", "Coccinellidae", "Adalia, Harmonia", "#ff2200")
    #insertRowInsects("Mosquito", "Culicidae", "Anophelinae, Culicinae", "#84838a")
    
    #print(searchInsects("Butterfly"))
    #print(searchUsers("jalarcon", "12345"))
    #print(searchUsers("jalarcon", "4526"))
    #print(searchUsers("pepe", "12345"))

    #insertRowInferencia("Butterfly", 3.3638927, -76.6255511, "#ffaa00","jalarcon", 1)
    #insertRowInferencia("Dragonfly", 3.3638927, -76.5255511, "#0066ff","jalarcon", 0)  
    #insertRowInferencia("Grasshopper", 3.3638927, -76.5255511, "#00ff11","grivera", 1)
    #insertRowInferencia("Ladybird", 3.3638927, -76.5255511, "#ff2200","grivera", 0)  
    #print(readRowsInferencia())

    #insertRowBlog("jalarcon","Hoy visitando el parque de la flora me encontré una abeja tomando agua","Fue genial")
    pass