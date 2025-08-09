from db.db_connection import get_connection

def insertar_usuario(nombre, edad):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)", (nombre, edad))
    conn.commit()
    cur.close()
    conn.close()

def obtener_usuarios():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, nombre, edad FROM usuarios")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data


def insertar_producto(nombre, categoria, cantidad, costo_unitario, precio_publico, precio_publico_vip):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"INSERT INTO tbl_producto (nombre, categoria, cantidad, costo_unitario, precio_publico, precio_publico_vip) VALUES (%s, %s, %s, %s, %s, %s)",(nombre,categoria,cantidad,costo_unitario,precio_publico,precio_publico_vip))
    conn.commit()
    cur.close()
    conn.close()

def obtener_productos():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM tbl_producto")
    data = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return data