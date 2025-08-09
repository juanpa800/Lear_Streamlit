# Para editar y ejecutar el proyecto

1. Instala las dependencias, se recomienda utilizar un entorno virtual
    pip install -r requirements.txt
2. Servir la aplicación 
    streamlit run app.py
3. Configure la base de datos, para esto se recomienda establecer variables de entorno y ejecutar los queries db_structure.py que se encargan de crear las tablas de la base de datos
4. Mantenga la siguiente estructura
 ```py
mi_app/
├── app.py                      # App principal de Streamlit
├── config/
│   └── db_config.py            # Configuración de la base de datos
|   └── db_structure.py         # Configuración inical: creacion de tablas 
├── db/
│   └── db_connection.py        # Funciones para conectarse a PostgreSQL
│   └── queries.py              # Funciones con consultas SQL
├── pages/
│   └── ver_usuarios.py         # Módulos adicionales con páginas (opcional)
├── requirements.txt            # Dependencias del proyecto: pip freeze > requirements.txt
└── README.md                   # Documentación del proyecto
```
