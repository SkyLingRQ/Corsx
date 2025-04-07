<h1 align="center">Corsx</h1>

Corsx es una herramienta desarrollada en Python para el escaneo individual o masivo de URLs con el objetivo de detectar posibles vulnerabilidades en la configuración de Cross-Origin Resource Sharing (CORS). Gracias a su implementación basada en asyncio y aiohttp, permite realizar pruebas de forma concurrente y altamente eficiente, reduciendo considerablemente los tiempos de análisis.

# Instalación
```bash
git clone https://github.com/SkyLingRQ/Corsx.git
cd Corsx
python3 -m pip install -r requirements.txt
```

# Uso

```bash
usage: corsx.py [-h] [-u URL] [-f FILE]

C O R S - EviLight

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     Scanning a URL
  -f FILE, --file FILE  Scanning using files with URLs
```
Para escanear una lista de URLs
```bash
python3 corsx.py -f tu_archivo.txt
```
Para el escaneo individual de una sola URL
```bash
python3 corsx.py -u https://www.example.com
```
