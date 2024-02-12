# Dependencias a instalar
pip install nextcord
pip install aiosqlite
pip install python-dotenv
Todo el registro se lleva en el task1 de sprint1

# Env init
    Configuración del Entorno Virtual:
        - Abre una terminal o línea de comandos.
        - Crea un nuevo directorio para tu proyecto y navega a él.
        - Ejecuta `python3 -m venv venv` para crear un entorno virtual llamado `venv`.
    Activa el entorno virtual:
        - En Windows: **`.\venv\Scripts\activate`**
        - En macOS/Linux: **`source venv/bin/activate`**

#  utilización de DotEnv para isolar tokens e información confidencial
        from dotenv import load_dotenv
        load_dotenv()
        token = os.getenv('DISCORD_TOKEN')
