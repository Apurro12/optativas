import sys 
import io
import shutil
import re
import os
import subprocess
import shlex

class student:
    def __init__(self,array):
        self.data = []
        array_sep = array.split("\t")
        status_materias_1 = []
        status_materias_2 = []
        status_materias_3 = []
        status_materias_4 = []
        status_optativas = []
        intencion_optativas = []
        #print(array_sep)
        self.fecha = array_sep[0] 
        self.nombre = array_sep[1]
        self.apellido = array_sep[2]
        self.numAlumno = array_sep[3]
        self.email = array_sep[4]
#esto se puede mejorar usando dictionaries
        for i in range(len(materias_1)):
        	status_materias_1.append(array_sep[5+i])
        self.Primero = status_materias_1
        for i in range(len(materias_2)):
        	status_materias_2.append(array_sep[5+len(materias_1)+i])
        self.Segundo = status_materias_2
        for i in range(len(materias_3)):
        	status_materias_3.append(array_sep[5+len(materias_1)+len(materias_2)+i])
        self.Tercero = status_materias_3
        for i in range(len(materias_4)):
        	status_materias_4.append(array_sep[5+len(materias_1)+len(materias_2)+len(materias_3)+i])
        self.Cuarto = status_materias_4
        opt = array_sep[5+len(materias_1)+len(materias_2)+len(materias_3)+len(materias_4)].split(",")
#		for i in range(len(opt)):
#			status_optativas.append(opt[i])
        self.Optativas = opt
        optIntencion = array_sep[5+len(materias_1)+len(materias_2)+len(materias_3)+len(materias_4)+1].split(", ")
#		for i in range(len(optIntencion)):
#			intencion_optativas.append(optIntencion[i])
        TodoCursado = status_materias_1+status_materias_2+status_materias_3+status_materias_4+opt
        
        self.TodoCursado = TodoCursado
        self.Cursar = optIntencion


        
    def check(self):
        def appendAndPrint(name,listOfCorrs,listOfNames):
            if 'NC' not in listOfCorrs and 'EC' not in listOfCorrs:
                puedeCursar.append(name)
            if 'NC' not in listOfCorrs and 'EC' in listOfCorrs:
                condicional.append(name)
            if any(name in s for s in self.Cursar):
                for i in range(len(listOfCorrs)):
                    #for j in self.Optativas:
                    #    if any(j in s for s in listOfCorrs):
                    #        print(j)
                    #        print("7777777777777")
                    #if( i == self.Optativas):
                    #    print("7777777777777")
                    #    print(self.Optativas)
#                    if(listOfCorrs[i] == "A" or listOfCorrs[i] == "TP" or listOfCorrs[i] == "EC"):
#                        puedeCursar.append(name)
#                        break
                    if(listOfCorrs[i] == "NC"):
                        print("No tiene "+listOfNames[i]+" que se requiere para cursar "+name+".")
                    if(listOfCorrs[i] == "EC"):
                        print("Ojo! Para cursar "+name+" necesita "+listOfNames[i]+" y la esta cursando.")
        nuevas = []
        puedeCursar = []
        condicional = []
        corrMecanicaII = ["Mecánica Analítica"] #materias_3[0]
        corrMecanicaEstadisticaII = ["Mecánica Estadística I"] #materias_4[2]
        corrMetodosdelaFisicaMatematica = ["Matemáticas Especiales II"] #materias_3[1]
        corrSeminariodeFisicadelSolido = ["Mecánica Estadística I"] #materias_4[2]
        corrSeminariodeParticulasyCampos = ["Mecanica Cuántica II"] #materias_4[0]
        corrSeminariodeMecanicaCuantica = ["Mecanica Cuántica II","Mecánica Estadística I"] #materias_4[0], materias_4[2]
        corrSeminariodeOpticaAvanzada = ["Electromagnetismo","Mecánica Cuántica I"] # materias_3[2]
        corrSeminariodeFisicaNuclear = ["Mecanica Cuántica II","Mecánica Estadística I","Experimentos Cuánticos II"] #materias_4[0], materias_4[2], materias_4[1]
        corrSimulacionesComputacionalesenFisica = ["Mecánica Estadística I"] #materias_4[2]
        corrTermodinamica = ["Física General IV","Física Experimental IV","Matemáticas Especiales I","Física Macroscópica"] #materias_2[3],materias_2[4],materias_2[5],materias_2[6],
        corrTopicosdeMateriaCondensada = ["X"]
        print('\n'+"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print("Situacion del alumno "+self.nombre+" "+self.apellido+" con numero de alumno "+self.numAlumno)
        print("Conflictos: ")
        
        listaOptativas = ["Mecánica II","Mecánica Estadísitica II","Métodos de la Física Matemática","Seminario de Física del Sólido","Seminario de Partículas y Campos","Seminario de Mecánica Cuántica","Seminario de Optica Avanzada","Seminario de Física Nuclear","Simulaciones Computacionales en Física","Termodinámica","Álgebra lineal: Aplicaciones Físicas", "Electromagnetismo 2", "Elementos de la Teoría Cuántica de Campos", "Introducción a la Relatividad General", "Física de la Materia Blanda", "Tópicos de Materia Condensada, ciencia de materiales y nanociencia", "Ciencia de Materiales y Nanociencia"]
        listaOptativas_FisMed = ["Procesos estocásticos y su aplicación al modelo de sistemas físicos, químicos y biológicos","Computación","Electrónica", "Análisis de Señales", "Biofísica"]
        listaOptativas_Bio = ["Biofisicoquímica","Biología"]
        listaOptativas_Mate = ["Geometría diferencial", "Elementos de matetmática aplicada", "Topología", "Análisis Numérico I","Geometría Diferencial","Geometria Diferencial","Elementos de mtemática aplicada - Geometría diferencial","Geometría diferencial (departamento de matemática)"]
        listaOptativas_Obser = ["Computación (observatorio)","computación (observatorio)", "Computación de Astronomía" ,"Dinámica no lineal","Análisis Numérico","Introducción a la Astrofísica Relativista","Computación (Observatorio)"]
        listaOptativas_Posgrado = ["Métodos de geometría diferencial en Teoría de la Información","Probabilidades y estadísitca en Física Experimental"]


        for i in self.Cursar:
            if not any(i in s for s in listaOptativas):
                if not any(i in s for s in listaOptativas_Bio):
                    if not any(i in s for s in listaOptativas_Mate):
                        if not any(i in s for s in listaOptativas_Obser):
                            if not any(i in s for s in listaOptativas_Posgrado):
                                nuevas.append(i)
        
        if any("Métodos de geometría diferencial en Teoría de la Información" in s for s in self.Cursar):
            appendAndPrint("Métodos de geometría diferencial en Teoría de la Información",[self.Cuarto[0],self.Cuarto[1],self.Cuarto[2],self.Tercero[0],self.Tercero[1],self.Tercero[2],self.Tercero[3],self.Tercero[4],self.Tercero[5]],[materias_4[0],materias_4[1],materias_4[2],materias_3[0],materias_3[1],materias_3[2],materias_3[3],materias_3[4],materias_3[5]])
        
        if any("Probabilidades y estadísitca en Física Experimental" in s for s in self.Cursar):
            appendAndPrint("Probabilidades y estadísitca en Física Experimental",[self.Cuarto[0],self.Cuarto[1],self.Cuarto[2],self.Tercero[0],self.Tercero[1],self.Tercero[2],self.Tercero[3],self.Tercero[4],self.Tercero[5]],[materias_4[0],materias_4[1],materias_4[2],materias_3[0],materias_3[1],materias_3[2],materias_3[3],materias_3[4],materias_3[5]])
        
        if any("Dinámica no lineal" in s for s in self.Cursar):
            appendAndPrint("Dinámica no lineal",[self.Tercero[1]],[materias_3[1]])
        
        if any("Análisis Numérico" in s for s in self.Cursar):
            appendAndPrint("Análisis Numérico",[listaOptativas[10],self.Segundo[2],listaOptativas_Obser[0]],[listaOptativas[10],materias_2[2],listaOptativas_Obser[0]])
        
        if any("Introducción a la Astrofísica Relativista" in s for s in self.Cursar):
            appendAndPrint("Introducción a la Astrofísica Relativista",[self.Tercero[0],self.Tercero[1],self.Tercero[2]],[materias_3[0],materias_3[1],materias_3[2]])
        
        if any(("Geometría diferencial" or "Elementos de mtemática aplicada - Geometría diferencial" or "Geometría diferencial (departamento de matemática)") in s for s in self.Cursar) or any("Geometría Diferencial" in s for s in self.Cursar) or any("Geometria Diferencial" in s for s in self.Cursar):
            appendAndPrint("Geometría diferencial",[listaOptativas[10],self.Tercero[1]],[listaOptativas[10],materias_3[1]])
        
        if any("Elementos de matemática aplicada" in s for s in self.Cursar):
            appendAndPrint("Elementos de matemática aplicada",[self.Primero[3],self.Primero[2]],[materias_1[3],materias_1[3]])
        
        if any("Topología" in s for s in self.Cursar):
            appendAndPrint("Topología",[self.Primero[3],self.Primero[2],listaOptativas[10]],[materias_1[3],materias_1[2],listaOptativas[10]])
        
        if any("Análisis Numérico I" in s for s in self.Cursar):
            #listaOptativas_Obser[0]  puse obser pero no se sabe bien cu'al 
            appendAndPrint("Análisis Numérico I",[listaOptativas[10],self.Segundo[2],listaOptativas_Obser[0]],[listaOptativas[10],materias_2[2],listaOptativas_Obser[0]])
        
        if any("Biología" in s for s in self.Cursar):
            appendAndPrint("Biología",[self.Primero[0],self.Primero[1],self.Primero[2],self.Primero[3],self.Primero[4],self.Primero[5],self.Segundo[0],self.Segundo[1],self.Segundo[2],self.Segundo[3],self.Segundo[4],self.Segundo[5],self.Segundo[6]],[materias_1[0],materias_1[1],materias_1[2],materias_1[3],materias_1[4],materias_1[5],materias_2[0],materias_2[1],materias_2[2],materias_2[3],materias_2[4],materias_2[5],materias_2[6]])

        if any("Biofisicoquímica" in s for s in self.Cursar):
            appendAndPrint("Biofisicoquímica",[self.Segundo[6],self.Segundo[0],listaOptativas[9]],[materias_2[6],materias_2[0],listaOptativas[9]])

        if any("Biofísica" in s for s in self.Cursar):
            appendAndPrint("Biofísica",[self.Segundo[0],self.Segundo[6]],[materias_2[0],materias_2[6]])
        
        if any("Procesos estocásticos y su aplicación al modelo de sistemas físicos, químicos y biológicos" in s for s in self.Cursar):
            appendAndPrint("Procesos estocásticos y su aplicación al modelo de sistemas físicos, químicos y biológicos",[self.Tercero[1],self.Cuarto[2]],[materias_3[1],materias_4[2]])
        
        if any(("Computación" or "Computación (Observatorio)" or "computación (observatorio)" or "Computación de Astronomía") in s for s in self.Cursar):
            appendAndPrint("Computación",[self.Primero[2],self.Segundo[0]],[materias_1[2],materias_2[0]])
        
        if any("Electrónica" in s for s in self.Cursar):
            appendAndPrint("Electrónica",[self.Segundo[0],self.Tercero[1]][materias_2[0],materias_3[1]])
        
        if any("Análisis de Señales" in s for s in self.Cursar):
            appendAndPrint("Análisis de Señales",[self.Segundo[0],self.Tercero[1]],[materias_2[0],materias_3[1]])
        
        if any("Álgebra lineal" in s for s in self.Cursar):
            appendAndPrint("Álgebra lineal",[self.Primero[3],self.Primero[0],self.Primero[2]],[materias_1[3],materias_1[0],materias_1[2]])
        
        if any("Electromagnetismo 2" in s for s in self.Cursar):
            appendAndPrint("Electromagnetismo 2",[self.Tercero[0],self.Tercero[1],self.Tercero[2],self.Tercero[3]],[materias_3[0],materias_3[1],materias_3[2],materias_3[3]])
        
        if any("Elementos de la Teoría Cuántica de Campos" in s for s in self.Cursar):
            appendAndPrint("Elementos de la Teoría Cuántica de Campos",[self.Cuarto[0],listaOptativas[2]],[materias_4[0],listaOptativas[2]])
        
        if any("Introducción a la Relatividad General" in s for s in self.Cursar):
            appendAndPrint("Introducción a la Relatividad General",[listaOptativas[11],listaOptativas[10]],[listaOptativas[11],listaOptativas[10]])
        
        if any("Física de la Materia Blanda" in s for s in self.Cursar):
            appendAndPrint("Física de la Materia Blanda",[self.Tercero[0],self.Tercero[1],self.Tercero[2],self.Tercero[3],self.Tercero[4],self.Tercero[5]],[materias_3[0],materias_3[1],materias_3[2],materias_3[3],materias_3[4],materias_3[5]])
        
        if any("Tópicos de Materia Condensada, ciencia de materiales y nanociencia" in s for s in self.Cursar) or any("Ciencia de Materiales y Nanociencia" in s for s in self.Cursar):
            appendAndPrint("Tópicos de Materia Condensada, ciencia de materiales y nanociencia",[listaOptativas[3],self.Cuarto[0],self.Tercero[0]],[listaOptativas[3],materias_4[0],materias_3[0]])
        
        if any("Mecánica II" in s for s in self.Cursar):
            appendAndPrint("Mecánica II",[self.Tercero[0]],[materias_3[0]])
        
        if any("Mecánica Estadísitica II" in s for s in self.Cursar):
            appendAndPrint("Mecánica Estadísitica II",[self.Cuarto[2]],[materias_4[2]])

        if any("Métodos de la Física Matemática" in s for s in self.Cursar):
            appendAndPrint("Métodos de la Física Matemática",[self.Tercero[1]],[materias_3[1]])
        
        if any("Seminario de Física del Sólido" in s for s in self.Cursar):
            appendAndPrint("Seminario de Física del Sólido",[self.Cuarto[2]],[materias_4[2]])
        
        if any("Seminario de Partículas y Campos" in s for s in self.Cursar):
            appendAndPrint("Seminario de Partículas y Campos",[self.Cuarto[0]],[materias_4[0]])
        
        if any("Seminario de Mecánica Cuántica" in s for s in self.Cursar):
            appendAndPrint("Seminario de Mecánica Cuántica",[self.Cuarto[0],self.Cuarto[2]],[materias_4[0],materias_4[2]])
        
        if any("Seminario de Optica Avanzada" in s for s in self.Cursar):
            appendAndPrint("Seminario de Optica Avanzada",[self.Tercero[2]],[materias_3[2]])
        
        if any("Seminario de Física Nuclear" in s for s in self.Cursar):
            appendAndPrint("Seminario de Física Nuclear",[self.Cuarto[0],self.Cuarto[1],self.Cuarto[2]],[materias_4[0],materias_4[1],materias_4[2]])
        
        if any("Simulaciones Computacionales en Física" in s for s in self.Cursar):
            appendAndPrint("Simulaciones Computacionales en Física",[self.Cuarto[2]],[materias_4[2]])
        
        if any("Termodinámica" in s for s in self.Cursar):
            appendAndPrint("Termodinámica",[self.Segundo[3],self.Segundo[4],self.Segundo[5]],[materias_2[3],materias_2[4],materias_2[5]])
#		
#if any("Tópicos de Materia Condensada" in s for s in self.Cursar):
            

        self.PuedeCursar = puedeCursar
        self.Condicional = condicional
        
        print('------------------------------------------------'+'\n')
        print("Pidio Cursar: ")
        print(self.Cursar)
        print('\n'+"Puede cursar: ")
        print(puedeCursar)
        print('\n'+"Queda como condicional en: ")
        print(self.Condicional) 
        print('\n'+"Quiere cursar tambien la nueva materia:")
        print(nuevas)
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")


materias_1 = ["Física General I", "Física Experimental I", "Análisis Matemático I", "Algebra", "Física General II", "Física Experimental II"] 
materias_2 = ["Física General III", "Física Experimental III", "Análisis Matematico II", "Física General IV", "Física Experimental IV", "Matemáticas Especiales I", "Física Macroscópica"]
materias_3 = ["Mecánica Analítica", "Matemáticas Especiales II", "Electromagnetismo", "Experimentos Electromagnéticos", "Mecánica Cuántica I", "Experimentos Cuánticos I"]
materias_4 = ["Mecanica Cuántica II", "Experimentos Cuánticos II", "Mecánica Estadística I"]


def printFullInfo(allStudents):
	for i in range(len(allStudents)):
		print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
		print("El alumno "+allStudents[i].nombre+" ")
		print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

F = open("Resultados_2017.txt","r",encoding='utf-8') 

alumnos = []


i = 0
info = []
materia = []
for line in F:
    if i == 0:
	    #print(line.split("\t"))
        for j in line.split(" "):
            info.append(j)
    if i >0:
        alumno = student(line)
        alumnos.append(alumno)
    a = int(i)    
    i += 1
#    if i == 2:
#        break
#materia del primer anio:



materias_optativas= []

#print(info)
#printFullInfo(alumnos)
#print("fecha "+alumnos[0].fecha)
#print("Nombre "+alumnos[0].nombre)
#print("Apellido "+alumnos[0].apellido)
#print("Numero de alumno "+alumnos[0].numAlumno)
#print("email "+alumnos[0].email)
#print(""+alumnos[0].fecha)
for i in range(len(alumnos)):
	alumnos[i].check()

listaOptativas = ["Mecánica II","Mecánica Estadísitica II","Métodos de la Física Matemática","Seminario de Física del Sólido","Seminario de Partículas y Campos","Seminario de Mecánica Cuántica","Seminario de Optica Avanzada","Seminario de Física Nuclear","Simulaciones Computacionales en Física","Termodinámica","Álgebra lineal: Aplicaciones Físicas", "Electromagnetismo 2", "Elementos de la Teoría Cuántica de Campos", "Introducción a la Relatividad General", "Física de la Materia Blanda", "Tópicos de Materia Condensada, ciencia de materiales y nanociencia"]
listaOptativas_FisMed = ["Procesos estocásticos y su aplicación al modelo de sistemas físicos, químicos y biológicos","Computación","Electrónica","Análisis de Señales", "Biofísica"]
listaOptativas_Bio = ["Biofisicoquímica","Biología"]
listaOptativas_Mate = ["Geometría diferencial", "Elementos de matetmática aplicada", "Topología", "Análisis Numérico I","Geometría Diferencial"]
listaOptativas_Obser = ["Computación","Dinámica no lineal","Análisis Numérico","Introducción a la Astrofísica Relativista","Computación (Observatorio)"]
listaOptativas_Posgrado = ["Métodos de geometría diferencial en Teoría de la Información","Probabilidades y estadísitca en Física Experimental"]


F = open("letter.tex","w")

F.write("\\documentclass{letter}\n")
F.write("\\usepackage{hyperref}\n")
#F.write("\\usepackage{multicolumn}\n")
F.write("\\usepackage[spanish]{babel}\n")
F.write("\\usepackage[utf8]{inputenc}\n")
F.write("\\signature{La comisi\\'on de optativas}\n")
F.write("\\address{La Plata, 1 de julio de 2017}\n")
F.write("\\date{}\n")
F.write("\\begin{document}\n")
F.write("\n")
F.write("\\begin{letter}{Sr. Jefe del Departamento de F\\'isica \\\\ Facultad de Ciencias Exactas, UNLP \\\\ Prof. Dr. Daniel Cabra \\\\ S/D}\n")
F.write("\\opening{}\n")

F.write("Nos dirigimos a Ud. en nuestra calidad de Comisión Asesora de Materias Optativas, a fin de elevar la nómina de alumnos autorizados a cursar Materias Optativas en el 2do Cuatrimestre de 2017. Siguiendo las recomendaciones aprobadas por el Consejo Departamental el 13 de Julio de 2015, presentamos, para cada Materia Optativa, dos listas:\n")
F.write("\\begin{enumerate}\n")
F.write("\\item Un listado con aquellos alumnos que antes de comenzar el Primer Cuatrimestre de 2017 cumplen con las correlatividades necesarias para cursar en el próximo cuatrimestre;\n")
F.write("\\item Otro con los alumnos que al momento de la preinscripción se encontraban cursando alguna de las materias correlativas para poder cursar las materias a las que se preinscribieron. Los mismos sólo podrán cursar las materias optativas solicitadas en caso de aprobar sus correlativas.\n")

F.write("\n")
F.write("Asimismo, no incluimos en esas listas los casos cuyas preinscripciones aconsejamos desaprobar. Consideramos importante informar al Consejo acerca de los motivos que nos llevaron a tomar esta decisión, enumerados debajo:\n")
F.write("\\end{enumerate}\n")

F.write("\n")
F.write("Solicitamos al Consejo que comunique a la brevedad las resoluciones tomadas.\n")
F.write("\n")
F.write("\\closing{Sin otro particular, lo saluda atentamente}\n")
F.write("\n")
#F.write("\ps\n")
#F.write("\n")
#F.write("P.S. You can find the full text of GFDL license at\n")
#F.write("\n")
#F.write("\\encl{Copyright permission form}\n")
#F.write("\n")
F.write("\\end{letter}\n")
F.write("\\end{document}\n")
F.close()

File = open("letter_materias.tex","w")
File.write('\\documentclass{article}\n') # python will convert \n to os.linesepFile.write("\\newpage\n")
File.write("\\usepackage[spanish]{babel}\n")
File.write("\\usepackage[utf8]{inputenc}\n")

File.write("\\begin{document}\n")

for j in range(0,len(listaOptativas)):
    print(" ")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    File.write("\\begin{tabular}{|l|l|l|}\n")
#    File.write("\\multicolumn{3}{c}{{}}".format(listaOptativas[j]))
    File.write("\\hline\n")
    File.write("\\hline\n")
    File.write("{}\\\\\\hline\n".format(listaOptativas[j]))

    print(listaOptativas[j])
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print('\n'+'Aprobados:')
    File.write("\\hline\n")
    File.write("APROBADOS & & \\\\\n")
    for i in range(0,len(alumnos)):
        if any(listaOptativas[j] in s for s in alumnos[i].PuedeCursar):
            print(alumnos[i].nombre+'\t'+alumnos[i].apellido+'\t'+alumnos[i].numAlumno)
            File.write("{}&{}&{}\\\\\n".format(alumnos[i].nombre,alumnos[i].apellido,alumnos[i].numAlumno))
    print('\n\n'+'Condicionales:')
    File.write("\\hline\n")
    File.write("\\hline\n")
    File.write("CONDICIONALES & & \\\\\n")
    File.write("\\hline\n")
    File.write("\\hline\n")
    for i in range(0,len(alumnos)):
        if any(listaOptativas[j] in s for s in alumnos[i].Condicional):
            print(alumnos[i].nombre+'\t'+alumnos[i].apellido+'\t'+alumnos[i].numAlumno)
            File.write("{}&{}&{}\\\\\n".format(alumnos[i].nombre,alumnos[i].apellido,alumnos[i].numAlumno))
    File.write("\\hline\n")
    File.write("\\hline\n")
    File.write("\\end{tabular}\n")        
    File.write("\n")        
    File.write("\\vspace{1cm}\n")        

for j in range(0,len(listaOptativas_FisMed)):
    File.write("\\begin{tabular}{|l|l|l|}\n")
#    File.write("\\multicolumn{3}{c}{{}}".format(listaOptativas_FisMed[j]))
    File.write("\\hline\n")
    File.write("\\hline\n")
    File.write("{}\\\\\\hline\n".format(listaOptativas_FisMed[j]))
    File.write("\\hline\n")
    File.write("APROBADOS & & \\\\\n")
    for i in range(0,len(alumnos)):
        if any(listaOptativas_FisMed[j] in s for s in alumnos[i].PuedeCursar):
            File.write("{}&{}&{}\\\\\n".format(alumnos[i].nombre,alumnos[i].apellido,alumnos[i].numAlumno))
    File.write("\\hline\n")
    File.write("\\hline\n")
    File.write("CONDICIONALES & & \\\\\n")
    File.write("\\hline\n")
    File.write("\\hline\n")
    for i in range(0,len(alumnos)):
        if any(listaOptativas_FisMed[j] in s for s in alumnos[i].Condicional):
            File.write("{}&{}&{}\\\\\n".format(alumnos[i].nombre,alumnos[i].apellido,alumnos[i].numAlumno))
    File.write("\\hline\n")
    File.write("\\hline\n")
    File.write("\\end{tabular}\n")        
    File.write("\n")        
    File.write("\\vspace{1cm}\n")        

for j in range(0,len(listaOptativas_FisMed)):
    print(" ")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print(listaOptativas_FisMed[j])
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print('\n'+'Aprobados:')
    for i in range(0,len(alumnos)):
        if any(listaOptativas_FisMed[j] in s for s in alumnos[i].PuedeCursar):
            print(alumnos[i].nombre+'\t'+alumnos[i].apellido+'\t'+alumnos[i].numAlumno)
    print('\n\n'+'Condionales:')
    for i in range(0,len(alumnos)):
        if any(listaOptativas_FisMed[j] in s for s in alumnos[i].Condicional):
            print(alumnos[i].nombre+'\t'+alumnos[i].apellido+'\t'+alumnos[i].numAlumno)

for j in range(0,len(listaOptativas_Bio)):
    File.write("\\begin{tabular}{|l|l|l|}\n")
#    File.write("\\multicolumn{3}{c}{{}}".format(listaOptativas_Bio[j]))
    File.write("\\hline\n")
    File.write("\\hline\n")
    File.write("{}\\\\\\hline\n".format(listaOptativas_Bio[j]))
    File.write("\\hline\n")
    File.write("APROBADOS & & \\\\\n")
    for i in range(0,len(alumnos)):
        if any(listaOptativas_Bio[j] in s for s in alumnos[i].PuedeCursar):
            File.write("{}&{}&{}\\\\\n".format(alumnos[i].nombre,alumnos[i].apellido,alumnos[i].numAlumno))
    File.write("\\hline\n")
    File.write("\\hline\n")
    File.write("CONDICIONALES & & \\\\\n")
    File.write("\\hline\n")
    File.write("\\hline\n")
    for i in range(0,len(alumnos)):
        if any(listaOptativas_Bio[j] in s for s in alumnos[i].Condicional):
            File.write("{}&{}&{}\\\\\n".format(alumnos[i].nombre,alumnos[i].apellido,alumnos[i].numAlumno))
    File.write("\\hline\n")
    File.write("\\hline\n")
    File.write("\\end{tabular}\n")        
    File.write("\n")        
    File.write("\\vspace{1cm}\n")        

for j in range(0,len(listaOptativas_Bio)):
    print(" ")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print(listaOptativas_Bio[j])
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print('\n'+'Aprobados:')
    for i in range(0,len(alumnos)):
        if any(listaOptativas_Bio[j] in s for s in alumnos[i].PuedeCursar):
            print(alumnos[i].nombre+'\t'+alumnos[i].apellido+'\t'+alumnos[i].numAlumno)
    print('\n\n'+'Condionales:')
    for i in range(0,len(alumnos)):
        if any(listaOptativas_Bio[j] in s for s in alumnos[i].Condicional):
            print(alumnos[i].nombre+'\t'+alumnos[i].apellido+'\t'+alumnos[i].numAlumno)

for j in range(0,len(listaOptativas_Mate)):
    File.write("\\begin{tabular}{|l|l|l|}\n")
#    File.write("\\multicolumn{3}{c}{{}}".format(listaOptativas_Mate[j]))
    File.write("\\hline\n")
    File.write("\\hline\n")
    File.write("{}\\\\\\hline\n".format(listaOptativas_Mate[j]))
    File.write("\\hline\n")
    File.write("APROBADOS & & \\\\\n")
    for i in range(0,len(alumnos)):
        if any(listaOptativas_Mate[j] in s for s in alumnos[i].PuedeCursar):
            File.write("{}&{}&{}\\\\\n".format(alumnos[i].nombre,alumnos[i].apellido,alumnos[i].numAlumno))
    File.write("\\hline\n")
    File.write("\\hline\n")
    File.write("CONDICIONALES & & \\\\\n")
    File.write("\\hline\n")
    File.write("\\hline\n")
    for i in range(0,len(alumnos)):
        if any(listaOptativas_Mate[j] in s for s in alumnos[i].Condicional):
            File.write("{}&{}&{}\\\\\n".format(alumnos[i].nombre,alumnos[i].apellido,alumnos[i].numAlumno))
    File.write("\\hline\n")
    File.write("\\hline\n")
    File.write("\\end{tabular}\n")        
    File.write("\n")        
    File.write("\\vspace{1cm}\n")        

for j in range(0,len(listaOptativas_Mate)):
    print(" ")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print(listaOptativas_Mate[j])
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    for i in range(0,len(alumnos)):
        if any(listaOptativas_Mate[j] in s for s in alumnos[i].PuedeCursar):
            print(alumnos[i].nombre+'\t'+alumnos[i].apellido+'\t'+alumnos[i].numAlumno)
    print('\n\n'+'Condionales:')
    for i in range(0,len(alumnos)):
        if any(listaOptativas_Mate[j] in s for s in alumnos[i].Condicional):
            print(alumnos[i].nombre+'\t'+alumnos[i].apellido+'\t'+alumnos[i].numAlumno)


for j in range(0,len(listaOptativas_Obser)):
    File.write("\\begin{tabular}{|l|l|l|}\n")
#    File.write("\\multicolumn{3}{c}{{}}".format(listaOptativas_Obser[j]))
    File.write("\\hline\n")
    File.write("\\hline\n")
    File.write("{}\\\\\\hline\n".format(listaOptativas_Obser[j]))
    File.write("\\hline\n")
    File.write("APROBADOS & & \\\\\n")
    for i in range(0,len(alumnos)):
        if any(listaOptativas_Obser[j] in s for s in alumnos[i].PuedeCursar):
            File.write("{}&{}&{}\\\\\n".format(alumnos[i].nombre,alumnos[i].apellido,alumnos[i].numAlumno))
    File.write("\\hline\n")
    File.write("\\hline\n")
    File.write("CONDICIONALES & & \\\\\n")
    File.write("\\hline\n")
    File.write("\\hline\n")
    for i in range(0,len(alumnos)):
        if any(listaOptativas_Obser[j] in s for s in alumnos[i].Condicional):
            File.write("{}&{}&{}\\\\\n".format(alumnos[i].nombre,alumnos[i].apellido,alumnos[i].numAlumno))
    File.write("\\hline\n")
    File.write("\\hline\n")
    File.write("\\end{tabular}\n")        
    File.write("\n")        
    File.write("\\vspace{1cm}\n")        

for j in range(0,len(listaOptativas_Obser)):
    print(" ")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print(listaOptativas_Obser[j])
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    for i in range(0,len(alumnos)):
        if any(listaOptativas_Obser[j] in s for s in alumnos[i].PuedeCursar):
            print(alumnos[i].nombre+'\t'+alumnos[i].apellido+'\t'+alumnos[i].numAlumno)
    print('\n\n'+'Condionales:')
    for i in range(0,len(alumnos)):
        if any(listaOptativas_Obser[j] in s for s in alumnos[i].Condicional):
            print(alumnos[i].nombre+'\t'+alumnos[i].apellido+'\t'+alumnos[i].numAlumno)


for j in range(0,len(listaOptativas_Posgrado)):
    File.write("\\begin{tabular}{|l|l|l|}\n")
#    File.write("\\multicolumn{3}{c}{{}}".format(listaOptativas_Posgrado[j]))
    File.write("\\hline\n")
    File.write("\\hline\n")
    File.write("{}\\\\\\hline\n".format(listaOptativas_Posgrado[j]))
    File.write("\\hline\n")
    File.write("APROBADOS & & \\\\\n")
    for i in range(0,len(alumnos)):
        if any(listaOptativas_Posgrado[j] in s for s in alumnos[i].PuedeCursar):
            File.write("{}&{}&{}\\\\\n".format(alumnos[i].nombre,alumnos[i].apellido,alumnos[i].numAlumno))
    File.write("\\hline\n")
    File.write("\\hline\n")
    File.write("CONDICIONALES & & \\\\\n")
    File.write("\\hline\n")
    File.write("\\hline\n")
    for i in range(0,len(alumnos)):
        if any(listaOptativas_Posgrado[j] in s for s in alumnos[i].Condicional):
            File.write("{}&{}&{}\\\\\n".format(alumnos[i].nombre,alumnos[i].apellido,alumnos[i].numAlumno))
    File.write("\\hline\n")
    File.write("\\hline\n")
    File.write("\\end{tabular}\n")        
    File.write("\n")        
    File.write("\\vspace{1cm}\n")        

for j in range(0,len(listaOptativas_Posgrado)):
    print(" ")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print(listaOptativas_Posgrado[j])
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    for i in range(0,len(alumnos)):
        if any(listaOptativas_Posgrado[j] in s for s in alumnos[i].PuedeCursar):
            print(alumnos[i].nombre+'\t'+alumnos[i].apellido+'\t'+alumnos[i].numAlumno)
    print('\n\n'+'Condionales:')
    for i in range(0,len(alumnos)):
        if any(listaOptativas_Posgrado[j] in s for s in alumnos[i].Condicional):
            print(alumnos[i].nombre+'\t'+alumnos[i].apellido+'\t'+alumnos[i].numAlumno)
File.write("\\end{document}\n")
File.close()
proc=subprocess.Popen(shlex.split('pdflatex letter.tex'))
proc.communicate()

proc=subprocess.Popen(shlex.split('pdflatex letter_materias.tex'))
proc.communicate()
bashCommand = "pdfunite letter.pdf letter_materias.pdf cartaConsejo.pdf"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output = process.communicate()[0]

