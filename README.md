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

```
    git clone https://github.com/pmoracho/tblrender.git
    cd tblrender
    python3 -m venv .venv --prompt=tblrender

    # En Windows
    .venv\Scripts\activate.bat

    # En Linux
    source .venv/bin/activate

    # Actualizar pip y setuptools
    python -m pip install --upgrade pip
    pip install --upgrade setuptools

    # Instalar  paquetes requeridos
    pip install -r requirements.txt
```

## 2. Despliegue

Para desplegar el script en el entorno activo:

    python setup.py develop

Lo que genera el script `tblrender` en el entorno actual. Pude invocarse
manualmente `tblrender` con el entorno activado, o bien puede invocarse
directamente desde el path absoluto al script, por ejemplo:

    .venv/bin/tblrender

