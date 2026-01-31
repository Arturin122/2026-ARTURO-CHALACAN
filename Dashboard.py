"""
Dashboard de Programación Orientada a Objetos
Autor: Arturo Geovanny Chalacan Paspuel
Materia: Programación Orientada a Objetos

Descripción:
Este programa funciona como un Dashboard en consola que permite
organizar, visualizar y ejecutar los scripts de las diferentes
unidades de la materia Programación Orientada a Objetos.
"""

import os
import subprocess


def mostrar_codigo(ruta_script):
    """
    Muestra el código fuente de un script Python seleccionado
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("❌ El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"❌ Ocurrió un error al leer el archivo: {e}")
        return None


def ejecutar_codigo(ruta_script):
    """
    Ejecuta el script seleccionado en una nueva consola
    """
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Sistemas Unix/Linux
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"❌ Ocurrió un error al ejecutar el código: {e}")


def mostrar_menu():
    """
    Menú principal del Dashboard
    Adaptado para organizar las tareas y scripts
    de la materia Programación Orientada a Objetos
    """
    ruta_base = os.path.dirname(__file__)

    unidades = {
        '1': 'UNIDAD 1',
        '2': 'UNIDAD 2'
    }

    while True:
        print("\n===== DASHBOARD OOP DE ARTURO =====")
        for key in unidades:
            print(f"{key} - {unidades[key]}")
        print("0 - Salir")

        eleccion_unidad = input("Elige una unidad o '0' para salir: ")

        if eleccion_unidad == '0':
            print("👋 Saliendo del programa.")
            break
        elif eleccion_unidad in unidades:
            ruta_unidad = os.path.join(ruta_base, unidades[eleccion_unidad])
            mostrar_sub_menu(ruta_unidad)
        else:
            print("❌ Opción no válida. Intenta de nuevo.")


def mostrar_sub_menu(ruta_unidad):
    """
    Muestra las subcarpetas de una unidad seleccionada
    """
    try:
        sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]
    except FileNotFoundError:
        print("❌ La unidad no existe.")
        return

    while True:
        print("\n--- Submenú: Temas de la Unidad ---")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion = input("Elige una opción: ")

        if eleccion == '0':
            break
        else:
            try:
                indice = int(eleccion) - 1
                if 0 <= indice < len(sub_carpetas):
                    ruta_sub = os.path.join(ruta_unidad, sub_carpetas[indice])
                    mostrar_scripts(ruta_sub)
                else:
                    print("❌ Opción no válida.")
            except ValueError:
                print("❌ Opción no válida.")


def mostrar_scripts(ruta_sub_carpeta):
    """
    Muestra los scripts Python dentro de una subcarpeta
    """
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta)
               if f.is_file() and f.name.endswith('.py')]

    while True:
        print("\n--- Scripts de Programación Orientada a Objetos ---")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar")
        print("9 - Menú principal")

        eleccion = input("Elige un script: ")

        if eleccion == '0':
            break
        elif eleccion == '9':
            return
        else:
            try:
                indice = int(eleccion) - 1
                if 0 <= indice < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[indice])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        input("\nPresiona Enter para continuar...")
                else:
                    print("❌ Opción no válida.")
            except ValueError:
                print("❌ Opción no válida.")


# Programa principal
if __name__ == "__main__":
    mostrar_menu()
