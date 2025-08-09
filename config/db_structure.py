from db.db_connection import get_connection

try:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE tbl_producto (
        inventario_id SERIAL PRIMARY KEY,
        nombre VARCHAR(250) NOT NULL,
        categoria VARCHAR(50),
        cantidad INT NOT NULL CHECK (cantidad >= 0),
        costo_unitario NUMERIC(12,2) NOT NULL CHECK (costo_unitario >= 0),
        fecha_ingreso TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        precio_publico NUMERIC(12,2) NOT NULL CHECK (precio_publico >= 0),
        precio_publico_vip NUMERIC(12,2) NOT NULL CHECK (precio_publico_vip >= 0),
        estado INT DEFAULT 0       
    );
    """)

    conn.commit()
    print("✅ Tabla creada exitosamente.")

except Exception as e:
    print("❌ Error:", e)

finally:
    if cur:
        cur.close()
    if conn:
        conn.close()