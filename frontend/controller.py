import sqlite3 as sql

def createDB():
    conn = sql.connect("insects.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("insects.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE insects (
            nombreComun text,
            nombreCientifico text,
            divisionTaxonomica text,
            color text
        )"""
    )
    conn.commit()
    conn.close()

def createTableInferencia():
    conn = sql.connect("insects.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE inferencias (
            nombreComun text,
            latitud float,
            longitud float,
            color text
        )"""
    )
    conn.commit()
    conn.close()

def insertRowInsects(nombreComun,nombreCientifico,divisionTaxonomica,color):
    conn = sql.connect("insects.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO insects VALUES ('{nombreComun}','{nombreCientifico}','{divisionTaxonomica}','{color}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def insertRowInferencia(nombreComun,latitud,longitud,color):
    conn = sql.connect("insects.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO inferencias VALUES ('{nombreComun}',{latitud},{longitud},'{color}')"
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

if __name__ == "__main__":
    #createDB()
    #createTable()
    #createTableInferencia()
    #insertRowInsects("Butterfly", "Lepidopteros", "Diurnas (Rophalocero), Nocturnas (Heterocero)", "#ffaa00")
    #insertRowInsects("Dragonfly", "Anisopteros", "Zygoptera, Epiprocta", "#0066ff")
    #insertRowInsects("Grasshopper", "Orthoptera Caelifera", "Tridactyloidea,Tetrigoidea, Eumastacidae, Proscopiidae, Pneumoridae, Pyrgomorphidae, Acrididae + Pamphagidae", "#00ff11")
    #insertRowInsects("Ladybird", "Coccinellidae", "Adalia, Harmonia", "#ff2200")
    #insertRowInsects("Mosquito", "Culicidae", "Anophelinae, Culicinae", "#84838a")
    #print(searchInsects("Butterfly"))
    #insertRowInferencia("Butterfly", 3.3638927, -76.6255511, "#ffaa00")
    #insertRowInferencia("Dragonfly", 3.3638927, -76.5255511, "#0066ff")    
    #print(readRowsInferencia())
    pass