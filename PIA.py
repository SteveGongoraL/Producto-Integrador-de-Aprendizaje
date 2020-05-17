import time
import pandas as pd
import sys
import sqlite3
from sqlite3 import Error
separador = ("°°°" * 40) + "\n"
nomAlumnos=["Steve","Diana","Fernando","Gabriela","Krista","Sarahi","Cindy","Nayeli","Isaac","Mariana","Brayton","Jordan","Dinah","Oliver","Wally","Barton","Frank","Matthew","Wilson","Bruce","Clark","Barry","Arthur","Cisco","Tawne","Tony","Natasha","Billy","Scott","Wanda"]
calificacionesAlumnos={}

def crearTablas():
    conn=sqlite3.connect("Evidencia3.db")
    c= conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Materias (Clave INTEGER PRIMARY KEY, NombreMateria INTEGER NOT NULL);")
    c.execute("CREATE TABLE IF NOT EXISTS Calificaciones (Nombre TEXT NOT NULL,ClaveMateria INTEGER NOT NULL,Calificacion INTEGER NOT NULL, FOREIGN KEY(ClaveMateria) REFERENCES Materias(Clave));")
    conn.close()
def eliminarInvalidos():
    conn=sqlite3.connect("Evidencia3.db")
    mi_cursor = conn.cursor()
    query=("DELETE FROM Calificaciones WHERE Calificacion > 100")
    mi_cursor.execute(query)
    conn.commit()
    mi_cursor.close()
def insertarMaterias():
    try:
        with sqlite3.connect("Evidencia3.db") as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute("INSERT INTO Materias VALUES(1,'Programacion')")
            mi_cursor.execute("INSERT INTO Materias VALUES(2,'Base de Datos')")
            mi_cursor.execute("INSERT INTO Materias VALUES(3,'Contabilidad')")
            mi_cursor.execute("INSERT INTO Materias VALUES(4,'Redes')")
            mi_cursor.execute("INSERT INTO Materias VALUES(5,'Estadistica')")
    except Error as e:
        print(e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
def guardaCalificacion(elemento,clave,calificacion):
    try:
        with sqlite3.connect("Evidencia3.db") as conn:
            mi_cursor = conn.cursor()
            valores ={"nombre":elemento,"claveMateria":materias,"calificacion":calificacion}
            mi_cursor.execute("INSERT INTO Calificaciones VALUES(:nombre,:claveMateria,:calificacion)",valores)
    except Error as e:
        print(e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

darInicio = input("\n\nPresione '0' (cero) para desplegar el menu: \n")
crearTablas()
insertarMaterias()
while darInicio>="0":
    print("\nMENU de opciones: \n\n1)- Mostrar o capturar los nombres de alumnos.\n2)- Capturar calificaciones.\n3)- Comprobar las asignaturas con el menor desempeño.\n4)- Calificaciones de estudiantes que reprobaron.\n5)- Mostrar datos completos.\n6)- Estadísticas descriptivas por materia o por estudiante\n7)- Guardar & salir.\n ")
    print(separador)
    opcion = input("¿Que operacion deseas realizar?: \n")
    if opcion == "1":
        carga=int(input("¿Que opcion desea realizar?\n1)- Capturar direfentes nombres.\n2)- Cargar los nombres predeterminados.\n\n"))
        if carga==1:
            del nomAlumnos[0:31]
            for i in range(1,31):
                nombre= input("Ingrese el nombre del alumno: ")
                nomAlumnos.append(nombre.title())
                print(f"{i*1} Alumnos registrados\n")
        else:
            print("Se cargaron los siguientes nombres de alumnos: ")
            print(nomAlumnos)
            longitud=(len(nomAlumnos))
            print('\n', longitud, "Alumnos registrados")
        time.sleep(3)
    elif opcion =="2":
        for elemento in nomAlumnos:
            calificacion1= float(input(f"Dime la calificacion en Programacion para {elemento}: "))
            materias=1
            guardaCalificacion(elemento,materias,calificacion1)
            while calificacion1<0 or calificacion1>100:
                print("Debes seleccionar una calificacion valida")
                calificacion1= float(input(f"Dime la calificacion en Programacion para {elemento}: "))
                materias=1
                guardaCalificacion(elemento,materias,calificacion1)
            else:
                print()
            calificacion2= float(input(f"Dime la calificacion en Base De Datos para {elemento}: "))
            materias=2
            guardaCalificacion(elemento,materias,calificacion2)
            while calificacion2<0 or calificacion2>100:
                print("Debes seleccionar una calificacion valida")
                calificacion2= float(input(f"Dime la calificacion en Base De Datos para {elemento}: "))
                materias=2
                guardaCalificacion(elemento,materias,calificacion2)
            else:
                print()
            calificacion3= float(input(f"Dime la calificacion en Contabilidad para {elemento}: "))
            materias=3
            guardaCalificacion(elemento,materias,calificacion3)
            while calificacion3<0 or calificacion3>100:
                print("Debes seleccionar una calificacion valida")
                calificacion3= float(input(f"Dime la calificacion en Contabilidad para {elemento}: "))
                materias=3
                guardaCalificacion(elemento,materias,calificacion3)
            else:
                print()
            calificacion4= float(input(f"Dime la calificacion en Redes para {elemento}: "))
            materias=4
            guardaCalificacion(elemento,materias,calificacion4)
            while calificacion4<0 or calificacion4>100:
                print("Debes seleccionar una calificacion valida")
                calificacion4= float(input(f"Dime la calificacion en Redes para {elemento}: "))
                materias=4
                guardaCalificacion(elemento,materias,calificacion4)
            else:
                print()
            calificacion5= float(input(f"Dime la calificacion en Estadistica para {elemento}: "))
            materias=5
            guardaCalificacion(elemento,materias,calificacion5)
            while calificacion5<0 or calificacion5>100:
                print("Debes seleccionar una calificacion valida")
                calificacion5= float(input(f"Dime la calificacion en Estadistica para {elemento}: "))
                materias=5
                guardaCalificacion(elemento,materias,calificacion5)
            else:
                print()
                print(separador)
                eliminarInvalidos()
                calificacionesAlumnos[elemento]=[calificacion1,calificacion2,calificacion3,calificacion4,calificacion5]
                notasEnDiccionario=pd.DataFrame(calificacionesAlumnos)
        notasEnDiccionario.index = ["Programacion", "Base de datos", "Contabilidad", "Redes", "Estadistica"]
    elif opcion =="3":
        print("Estadistica descriptiva calificacion mas baja de cada materia: ")
        print(notasEnDiccionario.T.min())
        print("\nMedia de todas las calificaciones por materia")
        print(notasEnDiccionario.T.mean())
        print("\nDesviacion estandar por todas las materias")
        print(notasEnDiccionario.T.std())
        print(separador)
        time.sleep(4)
    elif opcion =="4":
        print("Calificaciones de studiantes que reprobaron")
        aprobados = notasEnDiccionario.T[notasEnDiccionario.T<70]
        print(aprobados)
        print(separador)
        time.sleep(4)
    elif opcion =="5":
        print(notasEnDiccionario.T)
        print(separador)
        time.sleep(4)
    elif opcion =="6":
        decision=int(input("Quiere acceder a los datos estadisticos de: \n1)- Materias.\n2)- Estudiantes.\n"))
        if decision==1:
            print("\n°°°°Estadistica por materias°°°°")
            print(notasEnDiccionario.T.describe())
            op=int(input("¿Deseas guardar estos datos en un archivo de texto?\n1)- Obvio.\n2)- No gracias.\n"))
            if op==1:
                f = open("EstadisticaM.txt","w")
                f.write('--- Estadistica Descriptiva por Materia ---\n\n'+'% s'%notasEnDiccionario.T.describe())
                f.close()
                print("Se guardaron en un archivo llamado 'EstadisticaM'")
            else:
                print()
        else:
            print("\n°°°°Estadistica por alumnos°°°°")
            print(notasEnDiccionario.describe())
            op1=int(input("¿Deseas guardar estos datos en un archivo de texto?\n1)- Obvio.\n2)- No gracias.\n"))
            if op1==1:
                f = open("EstadisticaA.txt","w")
                f.write('--- Estadistica Descriptiva por Alumnos ---\n\n'+'% s'%notasEnDiccionario.describe())
                f.close()
                print("Se guardaron en un archivo llamado 'EstadisticaA'")
            else:
                print()
    elif opcion =="7":
        print("°°°Las calificaciones de los alumnos quedo guardada en una Base de Datos con nombre 'Evidencia3.db'°°°")
        break
    else:
        print("Debes de elegir una opción valida\n ")
else:
    print("Programa Terminado.\nDebes presionar el numero '0' para iniciar")