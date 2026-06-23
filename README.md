# TPI - Virtualización con VirtualBox (Arquitectura y Sistemas Operativos)

Trabajo Práctico Integrador de la materia **Arquitectura y Sistemas Operativos** (TUPaD - UTN). Consiste en crear una máquina virtual con Ubuntu usando VirtualBox y desarrollar dentro de ella un programa en Python.

## Contenido del repositorio

```
├── informe/
│   └── informe_tpi_virtualizacion.pdf   # Informe técnico
├── src/
│   └── suma_promedio.py                 # Código fuente del programa
├── capturas/
│   └── ...                              # Capturas de pantalla del proceso
└── README.md
```

## Descripción del programa

`suma_promedio.py` solicita al usuario 5 números enteros positivos (validando que sean enteros y mayores a 0), calcula la suma total y el promedio, y muestra ambos resultados por consola.

## Tecnologías utilizadas

- **VirtualBox** – software de virtualización
- **Ubuntu** (22.04) – sistema operativo invitado
- **Python 3** – desarrollo del programa

## Cómo ejecutar el programa

1. Clonar este repositorio (o copiar `src/suma_promedio.py` dentro de la VM).
2. Abrir una terminal en la máquina virtual con Ubuntu.
3. Ejecutar:
   ```bash
   python3 src/suma_promedio.py
   ```
4. Ingresar los 5 números enteros positivos cuando se solicite.

## Autor

[Tu nombre] - TUPaD, UTN	
