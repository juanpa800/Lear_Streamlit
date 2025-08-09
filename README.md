1. Instala las dependencias, se recomienda utilizar un entorno virtual
    pip install -r requirements.txt
2. Servir la aplicación 
    streamlit run app.py
3. Mantenga la siguiente estructura

mi_app/
├── app.py                      # App principal de Streamlit
├── config/
│   └── db_config.py            # Configuración de la base de datos
├── db/
│   └── db_connection.py        # Funciones para conectarse a PostgreSQL
│   └── queries.py              # Funciones con consultas SQL
├── pages/
│   └── ver_usuarios.py         # Módulos adicionales con páginas (opcional)
├── requirements.txt            # Dependencias del proyecto: pip freeze > requirements.txt
└── README.md                   # Documentación del proyecto
    
4. base de datos