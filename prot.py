#Nombre: César Roberto Vázquez García.  Código: 214402659.   Carrera: LIEC.

import os
import sqlite3

def registrar():
    conexion  = sqlite3.connect('student.db')
    cursor = conexion.cursor()
    codigo = input("Ingrese su código:\r\n")
    hora_entrada = input("Indique la hora de entrada:\r\n")
    hora_salida = input("Indique la hora de salida:\r\n")
    cursor.execute("INSERT INTO students VALUES (?,?,?)", (codigo, hora_entrada, hora_salida))
    conexion.commit()
    conexion.close()

def consultar():
    conexion  = sqlite3.connect('student.db')
    cursor = conexion.cursor()
    if cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='students'"):
        cursor.execute("SELECT * FROM students ORDER BY rowid DESC LIMIT 10")
        lista = cursor.fetchall()
        print("\r\nImprimiendo últimos 10 registros.\r\n")
        for item in lista:
            print(item)
        print()
    else:
        print("Registros no encontrados.\r\n")

def main():
    if not os.path.isfile('student.db'):
        conexion  = sqlite3.connect('student.db')
        cursor = conexion.cursor()
        cursor.execute("CREATE TABLE students (codigo text, h_ingreso text, h_salida text)")
        conexion.commit()
        conexion.close()
    while 1:
        registrar()
        consultar()

main()