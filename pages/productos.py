import streamlit as st
import pandas as pd
from db.queries import insertar_producto, obtener_productos

# st.title("Formulario de Registro")

# nombre = st.text_input("Nombre")
# edad = st.number_input("Edad", min_value=0)

# if st.button("Guardar"):
#     insertar_usuario(nombre, edad)
#     st.success("Usuario guardado")

# st.write("Usuarios registrados:")
# try:
#     usuarios = obtener_usuarios()
#     for u in usuarios:
#         st.write(u)
# except Exception as e:
#     st.error(f"Ha ocurrido un error: {e}")



st.title("Productos")

if "loc_nuevo_producto" not in st.session_state:
    st.session_state.loc_nuevo_producto = False

if st.button("Nuevo Producto", key="nuevo_producto"):
    st.session_state.loc_nuevo_producto = True

if st.session_state.loc_nuevo_producto:
    nombre = st.text_input("Nombre")
    categoria = st.text_input("Categoria _(opcional)_")
    cantidad = st.number_input("Cantidad", min_value=0)
    costo_unitario = st.number_input("Costo unitario ($)")
    precio_publico = st.number_input("Precio publico ($)")
    precio_publico_vip = st.number_input("Precio VIP ($)")

    try:
        if st.button("Crear Producto", key="crear_producto"):
            insertar_producto(nombre, categoria, cantidad, costo_unitario, precio_publico, precio_publico_vip)
            st.success(f"Producto {nombre} agregado")
            st.session_state.loc_nuevo_producto = False
            productos = obtener_productos()
    except Exception as e:
        st.error(f"Ha ocurrido un error al insertar el producto: {e}")


try:
    productos = obtener_productos()
    if productos:
        st.subheader("Lista de Productos")
        productos_nombre_columnas = [
            "ID", "Nombre", "Categoria","Cantidad", 
            "Costo unidad", "Fecha ingreso", "Precio publico", 
            "Precio VIP", "Estado"
            ]

        df_productos = pd.DataFrame(productos, columns=productos_nombre_columnas)

        search = st.text_input("Buscar",placeholder="Ej: aguardiente")
        if search:  
            df_productos = df_productos[df_productos['Nombre'].str.contains(search, case=False, na=False)]
        
        st.dataframe(df_productos)
    else:
        st.info("No hay productos registrados.")
except Exception as e:
    st.error(f"Ha ocurrido un error al obtener los productos: {e}")