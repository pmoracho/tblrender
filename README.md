# tblrender

Tabular data multi format render

# Instalación

## Requerimientos básicos:

Tener instalado y funcionando:

* Git
* Python 3.x

## 1. Entorno inicial básico

* Clonar repositorio
* Crear entorno virtual
* Activar entorno virtual
* actualizar `pip`
* Instalar requerimientos

    git clone https://github.com/pmoracho/tblrender.git
    cd tblrender
    python -m venv .venv --prompt=tblrender

    # En Windows
    .venv\Scripts.activate.bat

    # En Linux
    source .venv/bin/activate

    python -m pip install --upgrade pip

    pip install -r requirements.txt

## 2. Despliegue

### Con pyinstaller

Para construir la carpeta de despliegue de la aplicación en Windows, en primer lugar, con eentorno activado, instalar [Pyinstaller][pyinstaller]:

    pip install pyinstaller

Luego simplemente ejecutar:

    windist.bat


La carpeta final con la herramienta y sus binarios es:

    scrapper\dist\tblrender

